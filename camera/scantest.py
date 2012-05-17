#!/usr/bin/python

import chameleon, numpy, os, time, cv, sys, math

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'image'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'lib'))
import scanner, cuav_util, cuav_mosaic, mav_position

from optparse import OptionParser
parser = OptionParser("scantest.py [options] <filename..>")
parser.add_option("--repeat", type='int', default=1, help="scan repeat count")
parser.add_option("--view", action='store_true', default=False, help="show images")
parser.add_option("--gamma", type='int', default=0, help="gamma for 16 -> 8 conversion")
parser.add_option("--yuv", action='store_true', default=False, help="use YUV conversion")
parser.add_option("--mosaic", action='store_true', default=False, help="build a mosaic of regions")
parser.add_option("--mavlog", default=None, help="flight log for geo-referencing")
parser.add_option("--boundary", default=None, help="search boundary file")
parser.add_option("--max-deltat", default=1.0, type='float', help="max deltat for interpolation")
parser.add_option("--max-attitude", default=0, type='float', help="max attitude geo-referencing")
(opts, args) = parser.parse_args()

class state():
  def __init__(self):
    pass

def process(files):
  '''process a set of files'''

  scan_count = 0
  num_files = len(files)
  region_count = 0

  if opts.mavlog:
    mpos = mav_position.MavInterpolator()
    mpos.set_logfile(opts.mavlog)
  else:
    mpos = None

  if opts.boundary:
    boundary = cuav_util.polygon_load(opts.boundary)
  else:
    boundary = None

  if opts.mosaic:
    mosaic = cuav_mosaic.Mosaic()

  for f in files:
    frame_time = cuav_util.parse_frame_time(f)
    if mpos:
      try:
        pos = mpos.position(frame_time, opts.max_deltat)
      except mav_position.MavInterpolatorDeltaTException:
        pos = None
    if f.endswith('.pgm'):
      pgm = cuav_util.PGM(f)
      im = pgm.array
      if pgm.eightbit:
        im_8bit = im
      else:
        im_8bit = numpy.zeros((960,1280,1),dtype='uint8')
        if opts.gamma != 0:
          scanner.gamma_correct(im, im_8bit, opts.gamma)
        else:
          scanner.reduce_depth(im, im_8bit)
      im_colour = numpy.zeros((960,1280,3),dtype='uint8')
      scanner.debayer_full(im_8bit, im_colour)
      im_640 = numpy.zeros((480,640,3),dtype='uint8')
      scanner.downsample(im_colour, im_640)
    else:
      im = cv.LoadImage(f)
      im_640 = cv.CreateImage((640, 480), 8, 3)
      cv.Resize(im, im_640)
      im_640 = numpy.ascontiguousarray(cv.GetMat(im_640))

    count = 0
    total_time = 0

    if opts.yuv:
      img_scan = numpy.zeros((480,640,3),dtype='uint8')
      scanner.rgb_to_yuv(im_640, img_scan)
    else:
      img_scan = im_640

    t0=time.time()
    for i in range(opts.repeat):
      regions = scanner.scan(img_scan)
      count += 1
    t1=time.time()

    if boundary and mpos:
      if pos is None:
        regions = []
      elif (opts.max_attitude != 0 and (
        math.fabs(pos.roll) > opts.max_attitude or math.fabs(pos.pitch) > opts.max_attitude)):
        regions = []        
      for i in range(len(regions)-1, -1, -1):
        r = regions[i]
        (lat, lon) = cuav_util.gps_position_from_image_region(r, pos)
        if cuav_util.polygon_outside((lat, lon), boundary):
          regions.pop(i)
    
    region_count += len(regions)
    scan_count += 1

    if opts.mosaic:
      mosaic.add_regions(regions, img_scan, f, pos)
    
    if opts.view:
      mat = cv.fromarray(img_scan)
      for (x1,y1,x2,y2) in regions:
        cv.Rectangle(mat, (x1,y1), (x2,y2), (255,0,0), 1)
      cv.ShowImage('Viewer', mat)
      cv.WaitKey(1)
      cv.WaitKey(1)

    total_time += (t1-t0)
    print('%s scan %f fps  %u regions [%u/%u]' % (
      f, count/total_time, region_count, scan_count, num_files))
    

if opts.view:
    cv.NamedWindow('Viewer')

# main program
state = state()

process(args)
cv.WaitKey()
cv.DestroyWindow('Viewer')
