#!/usr/bin/python
# -*- coding: utf-8 -*-

#####################################################################
# Fretwork                                                          #
# Copyright (C) 2006 Sami Kyöstilä                                  #
#               2009-2017 FoFiX Team                                #
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

"""
Logging module

Usage
-----

Configure the logger in your launcher::

    from fretwork import log

    # configure the logger
    log.configure('file.log')


Import and use it::

    import logging

    logger = logging.getLogger(__name__)
"""

import logging
from logging.handlers import RotatingFileHandler


def configure(log_filename):
    """Configure logging"""
    # create the logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # file handler
    handler_filename = log_filename
    handler_max = 1000000  # 1 Mo
    file_handler = RotatingFileHandler(handler_filename, 'a', handler_max, 1)
    file_handler.setLevel(logging.INFO)

    # set handlers
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # init logging
    logger.debug("Logging initialized")
