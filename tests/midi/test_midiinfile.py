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

import unittest

from fretwork.midi.MidiInFile import MidiInFile
from fretwork.midi.MidiToText import MidiToText


class MidiInFileTest(unittest.TestCase):

    def setUp(self):
        self.test_file = "tests/midi/drumtest_notes.mid"

    def test_init(self):
        MidiInFile(MidiToText(), self.test_file)

    def test_read(self):
        midi_in = MidiInFile(MidiToText(), self.test_file)
        midi_in.read()
