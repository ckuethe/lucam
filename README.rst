Lumenera(r) USB Camera Interface
================================

Lucam is a Python library that provides two interfaces to the Lumenera(r)
LuCam API:

* **API**, a low level ctypes interface to the lucamapi.dll or liblucam.so
  version 6, exposing the definitions/declarations found in the lucam.h C
  header.

* **Lucam**, a high level object interface wrapping most of the ctypes
  interface, featuring exception based error handling and numpy.array type
  images.

:Authors:
  `Christoph Gohlke <https://www.lfd.uci.edu/~gohlke/>`_
  `Chris Kuethe <https://github.com/ckuethe/>`_

:Organization:
  Laboratory for Fluorescence Dynamics. University of California, Irvine

:License: BSD 3-Clause

:Version: 2021.6.6

Requirements
------------
* `CPython >= 3.7 <https://www.python.org>`_
* `Numpy 1.15 <https://www.numpy.org>`_
* `Lumenera USB camera and drivers 6.0 <https://www.lumenera.com/>`_

Revisions
---------
2022.8.20
    Add Linux support
2021.6.6
    Remove support for Python 3.6 (NEP 29).
2020.1.1
    Remove support for Python 2.7 and 3.5.

Notes
-----
"Lumenera" is a registered trademark of Teledyne Lumenera (1).

Lucam is slowly being revived to add support for more camera types and
host platforms.

Lucam has been tested with the Lu165M monochrome camera on Windows, and Lt29059
on Linux.

Some LuCam API functions are not available in the Lucam wrapper due to
lack of documentation or hardware for testing.

Naming of functions, methods, and constants that have an equivalent in
the LuCam API follows the LuCam API conventions, else PEP8 is followed.

References
----------
1. `Teledyne Lumenera <https://www.lumenera.com/>`_
2. Teledyne Lumenera LuCAM SDK User's Manual, Teldyne Lumenera.
3. Lumenera Camera User's Manual Release 6.8.1, Teledyne Lumenera.
4. Lumenera Camera SDK (LINUX) v2.4.3, Teledyne Lumenera.

Examples
--------
>>> from lucam import Lucam
>>> camera = Lucam()
>>> image = camera.TakeSnapshot()
>>> camera.SaveImage(image, 'test.tif')
>>> camera.CameraClose()

Refer to the test() function at the end of the module for more examples.
