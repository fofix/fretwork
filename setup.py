#!/usr/bin/env python
#####################################################################
#                                                                   #
# Fretwork                                                          #
# Copyright (C) 2009-2019 FoFiX Team                                #
#                                                                   #
# This program is free software; you can redistribute it and/or     #
# modify it under the terms of the GNU General Public License       #
# as published by the Free Software Foundation; either version 2    #
# of the License, or (at your option) any later version.            #
#                                                                   #
# This program is distributed in the hope that it will be useful,   #
# but WITHOUT ANY WARRANTY; without even the implied warranty of    #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the     #
# GNU General Public License for more details.                      #
#                                                                   #
# You should have received a copy of the GNU General Public License #
# along with this program; if not, write to the Free Software       #
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,        #
# MA  02110-1301, USA.                                              #
#####################################################################

from setuptools import setup

from fretwork.version import version_number


try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    long_description = open('README.md').read()


setup(
    name='fretwork',
    version=version_number,
    description='Game library used by FoFiX, and FoF:R.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='FoFiX team',
    author_email='contact@fofix.org',
    license='GPLv2+',
    url='https://github.com/fofix/fretwork',
    packages=['fretwork', 'fretwork.midi'],
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='music engine fofix frets game',
    install_requires=[
        "Pygame<2.0",
        "PyOpenGL",
        "numpy;python_version>'3.6'",
    ],
    test_suite="tests",
)
