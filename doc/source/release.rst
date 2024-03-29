How to release
==============

Here is the release process for ``fretwork``:

- bump the version on a PR (``fretwork/version.py`` and ``source/conf.py``)::

   pip install bumpversion
   bumpversion --allow-dirty part

- make a tag
- make wheels (see below)
- upload sources and wheels on GitHub in a new release.


Linux
-----

1. Install dependencies:

- ``SDL 1.2``
- ``SDL_mixer``
- ``libsoundtouch``
- ``libvorbisfile``
- ``pkg-config``
- ``portmidi``

2. Install Python dependencies::

    pip install -r requirements.txt


3. make a wheel::

    python2 setup.py sdist
    python2 setup.py bdist_wheel --inplace


4. repeat 3 and 4 with ``python3``.


Windows (32 bits)
-----------------

Python 2.7
++++++++++

- Download & install `Python 2.7 32 bits (x86) <https://www.python.org/downloads/windows/>`_
- Download & install `Microsoft Visual C++ Compiler for Python 2.7 <http://aka.ms/vcpython27>`_ (9.0)
- Open a Visual C++ Compiler console (32 bits)


Python 3.6
++++++++++

- Download & install `Python 3.6 32 bits (x86) <https://www.python.org/downloads/windows/>`_
- Download `Microsoft Visual C++ 2015 <http://landinghub.visualstudio.com/visual-cpp-build-tools>`_
- Open a Visual C++ 2015 x86 x64 cross build tools command prompt


All
+++

- Go to the fretwork directory
- Copy the Windows dependency pack into ``win32``
- Install some python dependencies::

    pip.exe install setuptools wheel

- Make a wheel::

    python.exe setup.py sdist
    python.exe setup.py bdist_wheel
