# fretwork

[![Code Health](https://landscape.io/github/fofix/fretwork/master/landscape.svg?style=flat)](https://landscape.io/github/fofix/fretwork/master)
[![Build Status](https://travis-ci.org/fofix/fretwork.svg?branch=master)](https://travis-ci.org/fofix/fretwork)
[![Documentation Status](https://readthedocs.org/projects/fretwork/badge/?version=latest)](http://fretwork.readthedocs.io/en/latest/?badge=latest)


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

For Windows, you should use the [win32 dependency pack](http://fofix.net/downloads/fofix-win32-deppack-20130304-updated.zip) (to unzip into the win32 directory).


### Native modules

Some parts of `fretwork` are written in C or C++. These must be compiled
before you can start the game from source:

    python setup.py build_ext --inplace --force
