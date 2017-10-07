#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path

from DataTypeConverters import readBew as readBew_
from DataTypeConverters import readVar
from DataTypeConverters import varLen


class RawInstreamFile(object):
    """
    It parses and reads data from an input file. It takes care of big
    endianess, and keeps track of the cursor position. The midi parser
    only reads from this object. Never directly from the file.
    """

    def __init__(self, infile=''):
        """
        Midi files are usually pretty small, so it should be safe to
        copy them into memory.

        :param infile: name of the file where data come from.
        """
        if infile and os.path.isfile(infile):
            with open(infile, 'rb') as f:
                self.data = f.read()
        else:
            self.data = ''

        # start at beginning ;-)
        self.cursor = 0

    def setData(self, data=''):
        "Sets the data from a string."
        self.data = data

    def setCursor(self, position=0):
        "Sets the absolute position if the cursor"
        self.cursor = position

    def getCursor(self):
        "Returns the value of the cursor"
        return self.cursor

    def moveCursor(self, relative_position=0):
        "Moves the cursor to a new relative position"
        self.cursor += relative_position

    def nextSlice(self, length, move_cursor=1):
        "Reads the next text slice from the raw data, with length"
        c = self.cursor
        slc = self.data[c:c+length]
        if move_cursor:
            self.moveCursor(length)
        return slc

    def readBew(self, n_bytes=1, move_cursor=1):
        """
        Reads n bytes of date from the current cursor position.
        Moves cursor if move_cursor is true
        """
        return readBew_(self.nextSlice(n_bytes, move_cursor))

    def readVarLen(self):
        """
        Reads a variable length value from the current cursor position.
        Moves cursor if move_cursor is true
        """
        MAX_VARLEN = 4  # Max value varlen can be
        var = readVar(self.nextSlice(MAX_VARLEN, 0))
        # only move cursor the actual bytes in varlen
        self.moveCursor(varLen(var))
        return var
