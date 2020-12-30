# fretwork

[![Coverage Status](https://coveralls.io/repos/github/fofix/fretwork/badge.svg?branch=master)](https://coveralls.io/github/fofix/fretwork?branch=master)
[![Build Status](https://travis-ci.org/fofix/fretwork.svg?branch=master)](https://travis-ci.org/fofix/fretwork)
[![Documentation Status](https://readthedocs.org/projects/fretwork/badge/?version=latest)](http://fretwork.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/fretwork.svg)](https://pypi.org/project/fretwork/)


Shared code for FoFiX and FoF:R.


## Setup

### Dependencies

You'll need those packages to run tests:
* `glib`
* `sdl 1.2`
* `sdl_mixer 1.2`
* `libogg`
* `libvorbisfile`
* `libtheora`
* `soundtouch`

For Windows, you should use the [win32 dependency pack](https://www.dropbox.com/s/p8xv4pktq670q9i/fofix-win32-deppack-20130304-updated.zip?dl=0) (to unzip into the win32 directory).


### Native modules

Some parts of `fretwork` are written in C or C++. These must be compiled
before you can start the game from source:

    python setup.py build_ext --inplace --force


## Related links

* Read the doc: https://fretwork.readthedocs.io
* Report bugs: https://github.com/fofix/fretwork/issues
* Get the latest version: https://pypi.org/project/fretwork
