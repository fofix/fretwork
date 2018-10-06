#!/usr/bin/python
# -*- coding: utf-8 -*-

# FoFiX
# Copyright (C) 2017-2018 FoFiX team
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
        #log.configure(self.logfile.name, logging.INFO)
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

    def test_logger_warning_level(self):
        # configurer the logger in Warning level
        #log.configure(self.logfile.name, logging.WARNING)
        log.configure(self.logfile.name, 'WARNING')

        # log two messages
        logger = logging.getLogger(__name__)
        msg_info = "Test info log"
        msg_warning = "Test warning log"
        logger.info(msg_info)
        logger.warning(msg_warning)

        # read the log file
        log_msgs = self.logfile.readlines()
        self.assertEqual(len(log_msgs), 1)
        log_msg = log_msgs[0].decode()

        # check the log file content
        self.assertNotIn('INFO', log_msg)
        self.assertNotIn(msg_info, log_msg)
        self.assertIn('WARNING', log_msg)
        self.assertIn(msg_warning, log_msg)
