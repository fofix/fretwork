#!/usr/bin/python

import unittest

from fretwork.unicode import unicodify
from fretwork.unicode import utf8


class UnicodeTest(unittest.TestCase):

    def test_unicodify(self):
        simple_s = "Jurgen"
        accent_s = "Jürgen"
        simple_b = b"Jurgen"
        u_simple_s = unicodify(simple_s)
        u_accent_s = unicodify(accent_s)
        u_simple_b = unicodify(simple_b)

        self.assertIs(type(u_simple_s), str)
        self.assertIs(type(u_accent_s), str)
        self.assertIs(type(u_simple_b), str)
        self.assertEqual(u_simple_s, simple_s)
        self.assertEqual(u_accent_s, u_accent_s)
        self.assertEqual(u_simple_b, simple_s)

    def test_utf8(self):
        simple_s = "Jurgen"
        accent_s = "Jürgen"
        simple_b = b"Jurgen"
        u_simple_s = utf8(simple_s)
        u_accent_s = utf8(accent_s)
        u_simple_b = utf8(simple_b)

        self.assertIs(type(u_simple_s), bytes)
        self.assertIs(type(u_accent_s), bytes)
        self.assertIs(type(u_simple_b), bytes)
        self.assertEqual(u_simple_s, simple_b)
        self.assertEqual(u_accent_s, u_accent_s)
        self.assertEqual(u_simple_b, simple_b)
