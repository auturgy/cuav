=================================
Using the CanberraUAV Imagery Set
=================================
Sources
=======
`CanberraUAV <http://canberrauav.org.au/>`_
has collected a large number of images from the `UAV Challenge
<https://uavchallenge.org/>`_.

These collections serve as a convenient source of image data to use with
the cuav tools.

They can be found at:

-  http://uav.anu.edu.au/OBC2016/CanberraUAV/
-  http://uav.anu.edu.au/OBC2014/CanberraUAV/
-  http://uav.anu.edu.au/OBC2012/CanberraUAV/

Note these are large downloads (~10Gb per imagery set).

The images themselves are in pgm format, which can be used directly with the
:doc:`../getting_started/geosearch` tool, or converted to jpg/png format via the 
:doc:`../getting_started/pgm_conv` tool.

Running Through a Geosearch
===========================

After downloading (for example) the 2016 Dataset, the geosearch program can be started
with the following options:

===============================   =================================================
Argument                          Value                                             
===============================   ================================================= 
files                             <Raw subfolder>
--mavlog                          <flight.tlog file>
--mission                         <way.txt file>
--view                            True
===============================   ================================================= 

Or as shown below:

.. image:: geosearch_cuav.png

After clicking ``Start``, go to ``GEOSearch -> Start`` in the menu of the Mosiac window (see below image, start 
button in red).

Then follow the instructions as per :doc:`../getting_started/geosearch`
