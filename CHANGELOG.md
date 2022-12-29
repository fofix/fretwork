# Release notes

## 1.0.0 (unreleased)

- build(python): support python 3.9 & 3.10
- docs: the changelog is now in project root
- ci: remove Travis CI
- ci: use GitHub Actions
- feat(audio): start python 3 transition
- fix(version): use a semver compat version
- refactor: mixstream is now a dependency

Links:
- https://github.com/fofix/fretwork/releases/tag/1.0.0
- https://github.com/fofix/fretwork/milestone/4?closed=1

## 0.5.0 (2021-01-04)

- build(doc): add requirements for the doc
- build(requirements): update the Cython version
- build(requirements): update the NumPy version
- build(requirements): update the PyOpenGL version
- build(requirements): update the Pygame version
- build(setup): do not pin requirements
- build(setup): update classifiers for Python versions
- docs(readme): fix the Windows dependency pack link
- docs(readme): remove the landscape.io badge
- docs(setup): update contact information
- fix(mixstream,windows): replace `dprintf` with `fdprintf`

Links:
- https://github.com/fofix/fretwork/releases/tag/0.5.0
- https://github.com/fofix/fretwork/milestone/3?closed=1

## 0.4.0 (2019-02-10)

- build(requirements): pin versions
- build(requirements): remove `Pillow`
- ci(tests): compute coverage
- docs(modles): complete the `mixstream` doc
- docs(readme): add a PyPI badge
- docs: add release notes
- feat(log): make the log level customizable
- feat(midi): start python 3 transition
- fix(midi): use relative imports
- fix(midi): use the right syntax for exceptions
- fix(mixstream): init the `SDL_mixer`
- tests(midi): add some tests
- tests(task): add some tests

Links:
- https://github.com/fofix/fretwork/releases/tag/0.4.0
- https://github.com/fofix/fretwork/milestone/2?closed=1

## 0.3.0 (2017-11-09)

- build: add a command to build the doc
- build: add a command to run pytest
- build: generate wheels for linux (manylinux1) and macos
- ci(travis): run the Travis CI
- docs(readme): add a ReadTheDoc badge
- docs(readme): add a Travis badge
- docs: explain how to release
- docs: generate Sphinx doc from docstrings
- feat(log): use the `logging` module
- feat(midi): use new style classes
- feat(python): port the code to python 3
- feat: add UTF-8 encoding headers
- test: add tests

Links:
- https://github.com/fofix/fretwork/releases/tag/0.3.0
- https://github.com/fofix/fretwork/milestone/1?closed=1

## 0.2.0 (2015-11-22)

- build(windows): copy the DLLs into the wheel
- docs(readme): add a landscape.io badge
- docs(readme): explain how to install on linux and Windows
- feat(midi): import shared code
- feat(task): add the `TaskEngine.exit` method
- feat(timer): import shared code
- feat: set the version in `fretwork.__version__`
- fix(mixstream): remove Cython generated code
- fix: remove ISO-8859-1 encoding headers

Link: https://github.com/fofix/fretwork/releases/tag/0.2.0


## 0.1.1 (2015-09-21)

Initial release: import shared code from FoFiX and Frets on Fire (FoF):

- feat(audio): import shared code
- feat(log): import shared code
- feat(mixstream): import shared code
- feat(task): import shared code
- feat(unicode): import shared code

Link: https://github.com/fofix/fretwork/releases/tag/0.1.1
