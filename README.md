[![Code Health](https://landscape.io/github/fofix/fretwork/master/landscape.svg?style=flat)](https://landscape.io/github/fofix/fretwork/master)
# fretwork
Shared code for FoFiX and FoF:R

The goal of this project is to reduce the duplication of effort around developing 2 differant forks of Frets on Fire. In general the code moved into this repository will be cleaned up from either FoFiX or enhanced from FoF:R. Then each project will be changed to remove the old code use the version located here.

Installation on windows is fairly simple. Download the latest release wheel from the downloads section, and run the following in a command prompt:

`pip install fretwork-0.1.1-cp27-none-win32.whl`

(Make sure to be in the download location of the wheel, and that the filename matches the file downloaded.)


For linux download the source from the releases page then run the following command:
`pip install fretwork-0.1.1.zip`

You will need a c compiler, and the following dependancies(there may be more in future releases):
glib
sdl 1.2
sdl_mixer 1.2
libogg
libvorbisfile
libtheora
