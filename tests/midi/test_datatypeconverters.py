#!/usr/bin/python
# -*- coding: utf-8 -*-

# FoFiX
# Copyright (C) 2017 FoFiX team
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import sys
import unittest

from fretwork.midi.DataTypeConverters import readBew
from fretwork.midi.DataTypeConverters import readVar
from fretwork.midi.DataTypeConverters import toBytes
from fretwork.midi.DataTypeConverters import varLen


class DataTypeConvertersTest(unittest.TestCase):

    def test_toBytes_type(self):
        if sys.version_info.major == 2:
            value = bytes('áâãa')
        else:
            value = bytes('áâãa', 'utf-8')
        result = toBytes(value)
        self.assertIs(type(result), tuple)

    def test_readBew_keyerror(self):
        if sys.version_info.major == 2:
            value = bytes('aà')
        else:
            value = bytes('aà', 'utf-8')
        self.assertIs(readBew(value), 0)

    def test_readBew_type(self):
        value = b'a'
        result = readBew(value)
        self.assertIs(type(result), int)

    def test_readVar(self):
        if sys.version_info.major == 2:
            value = bytes('áâãa')
        else:
            value = bytes('áâãa', 'utf-8')
        self.assertEqual(readVar(value), 295821045191137)

    def test_varLen(self):
        self.assertEqual(varLen(97), 1)
        self.assertEqual(varLen(256), 2)
        self.assertEqual(varLen(20000), 3)
        self.assertEqual(varLen(2107151), 4)
