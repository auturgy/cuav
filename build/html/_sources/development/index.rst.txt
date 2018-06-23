===========
Development
===========

The cuav source code is available from https://github.com/CanberraUAV/cuav

Windows
=======

You need to have `Python
2.7 <http://www.python.org/download/releases/2.7/>`_
and `wxPython <http://www.wxpython.org/download.php>`_ installed first.

Next, open up a console in the Python scripts install path
(:file:`C:\\Python27\\Scripts` or similar). Use ``pip install [filepath]`` to install them

- `numPY <http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy>`_
- `Pillow (replaces
  PIL) <http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow>`_
- `OpenCV 2 <http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv>`_
- `lxml <http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml>`_
- `pyexiv2 <https://launchpad.net/pyexiv2>`_
- `MinGW <https://sourceforge.net/projects/mingw/files/latest/download>`_
- `libjpeg-turbo <https://sourceforge.net/projects/libjpeg-turbo/files/1.5.1/>`_ (choose the libjpeg-turbo-1.5.1-gcc.exe file)

After making the desired changes, cuav is required to be compiled 
into the Python directory (the modules won't work otherwise).
This needs to happen after any changes to the source code. See the
:file:`./windows/geosearchbuildrun.bat` and  
:file:`./windows/geotagbuildrun.bat` scripts for information on how
to build and run the cuav tools.

To create a one-click windows installer for cuav, run ``cuavWinBuild.bat``, 
which is in the ``./windows`` directory. The installer is created in the 
``./windows/output`` directory. The `Inno Setup <http://www.jrsoftware.org/isdl.php#stable>`_ 
program is required for this process and is assumed to be installed in the 
``C:\Program Files (x86)\Inno Setup 5\`` folder

Linux
=====

Follow the user installation instructions as per the
topic :doc:`../installing/index` (minus the ``pip install cuav`` step).

After making the desired changes, cuav is required to be installed. This needs to happen after any changes to the source code. This can be done by:

.. code:: bash

    python setup.py build install --user
    
    

.. toctree::
    :maxdepth: 1
