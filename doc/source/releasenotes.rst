Release notes
=============

0.5.0 (2021-01-04)
------------------

- Build: specify numpy versions according to Python versions
- Build: update classifiers (Python versions 3.7 & 3.8)
- Deps: add a requirements.txt file
- Deps: do not pin requirements in `setup.py`
- Deps: update Cython version
- Deps: update NumPy version
- Deps: update PyOpenGL version
- Deps: update Pygame version
- Doc: fix the Windows dependency pack link in the README file
- Setup: update contact information
- Windows: replace `dprintf` with `fdprintf` (MixStream)

Details: https://github.com/fofix/fretwork/milestone/3?closed=1


0.4.0 (2019-02-10)
------------------

- Pin versions
- Make the log level customizable
- Fix `SDL_mixer` init
- Syntax: fix relative imports in the `midi` module
- Python 3: fix an exception syntax in `midi.EventDispatcher`
- Python 3: Use python3 imports for `StringIO` and `StringType`
- Doc: remove the useless `midi` module content
- Doc: add the `mixstream.VorbisFileMixStream` content
- Tests: add some tests for `midi.MidiInFile`
- Tests: add some tests for `midi.DataTypeConverters`
- Tests: add some tests for the `Task` module
- Deps: remove `Pillow` from requirements

Details: https://github.com/fofix/fretwork/milestone/2?closed=1


0.3.0 (2017-11-09)
------------------

- use the `logging` module
- port the code to python 3
- add docs
- add tests
- release on PyPi

Details: https://github.com/fofix/fretwork/milestone/1?closed=1


0.2.0 (2015-11-22)
------------------

- Add the `midi` module
- add the `time` module
- remove compiled code
- add DLLs path for Windows


0.1.1 (2015-09-21)
------------------

Initial release
