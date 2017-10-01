#!/usr/bin/python
# -*- coding: utf-8 -*-

#####################################################################
# Fretwork                                                          #
# Copyright (C) 2009-2015 FoFiX Team                                #
#               2009 John Stumpo                                    #
#               2006 Sami Kyöstilä                                  #
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

'''
Functions for writing to the logfile.
'''

from __future__ import print_function
import os
import sys
import time
import warnings
import traceback

from fretwork.unicode import utf8

# Whether to output log entries to stdout in addition to the logfile.
quiet = True

# Variable to be set in init
logFile = None
_old_showwarning = None
_initTime = None

# TODO - Create global cmd arg facilties to handle these types of things.
if "-v" in sys.argv or "--verbose" in sys.argv:
    quiet = False

# Labels for different priorities, as output to the logfile.
labels = {
  "warn":   "(W)",
  "debug":  "(D)",
  "notice": "(N)",
  "error":  "(E)",
}

# Labels for different priorities, as output to stdout.
if os.name == "posix":
    displaylabels = {
      "warn":   "\033[1;33m(W)\033[0m",
      "debug":  "\033[1;34m(D)\033[0m",
      "notice": "\033[1;32m(N)\033[0m",
      "error":  "\033[1;31m(E)\033[0m",
    }
else:
    displaylabels = labels


def _init_logging():
    global _old_showwarning, _initTime

    _old_showwarning = warnings.showwarning
    warnings.showwarning = _showwarning

    _initTime = time.time()
    debug("Logging initialized: " + time.asctime())


def setLogfile(file):
    global logFile
    logFile = file
    _init_logging()


def _log(cls, msg):
    '''
    Generic logging function.
    @param cls:   Priority class for the message
    @param msg:   Log message text
    '''
    msg = utf8(msg)
    timeprefix = "[%12.6f] " % (time.time() - _initTime)
    if not quiet:
        print(timeprefix + displaylabels[cls] + " " + msg)
    print(timeprefix + labels[cls] + " " + msg, file=logFile)
    logFile.flush()  #stump: truncated logfiles be gone!


def error(msg):
    '''
    Log a major error.
    If this is called while handling an exception, the traceback will
    be automatically included in the log.
    @param msg:   Error message text
    '''
    if sys.exc_info() == (None, None, None):
        #warnings.warn("Log.error() called without an active exception", UserWarning, 2)  #stump: should we enforce this?
        _log("error", msg)
    else:
        _log("error", msg + "\n" + traceback.format_exc())


def warn(msg):
    '''
    Log a warning.
    @param msg:   Warning message text
    '''
    _log("warn", msg)


def notice(msg):
    '''
    Log a notice.
    @param msg:   Notice message text
    '''
    _log("notice", msg)


def debug(msg):
    '''
    Log a debug message.
    @param msg:   Debug message text
    '''
    _log("debug", msg)


def _showwarning(*args, **kw):
    '''A hook to catch Python warnings.'''
    warn("A Python warning was issued:\n" + warnings.formatwarning(*args, **kw))
    _old_showwarning(*args, **kw)
