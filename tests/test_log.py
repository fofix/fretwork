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

import logging
import os
import tempfile
import unittest

from fretwork import log


class ConfigureTest(unittest.TestCase):

    def setUp(self):
        self.logfile = tempfile.NamedTemporaryFile(delete=True)

    def test_logger(self):
        # configurer the logger
        log.configure(self.logfile.name)
        self.assertTrue(os.path.exists(self.logfile.name))

        # log a message
        logger = logging.getLogger(__name__)
        msg = "Test info log"
        logger.info(msg)

        # read the log file
        log_msg = self.logfile.readline().decode()
        self.assertIn('INFO', log_msg)
        self.assertIn(msg, log_msg)
