# -*- coding: utf-8 -*-

#####################################################################
# Fretwork                                                          #
# Copyright (C) 2012 FoFiX Team                                     #
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
Miscellaneous functions for helping us handle Unicode correctly in
the face of what we've done in the past.
"""

# python3 hack
try:
    UNICODE_EXISTS = bool(type(unicode))
except NameError:
    unicode = str


def unicodify(s):
    """
    Turns `s` into a Unicode string

    :param s: input string
    :return:  Unicode version of s
    """
    if isinstance(s, unicode):
        return s
    elif isinstance(s, str):
        # not used in python3
        try:
            return s.decode('utf-8')
        except UnicodeDecodeError:
            return s
    else:
        try:
            return unicode(s)
        except UnicodeDecodeError:
            return str(s)


def utf8(s):
    '''
    Turns s into a valid UTF-8 bytestring.
    @param s: input
    @return:  UTF-8-encoded version of s
    '''
    return unicodify(s).encode('utf-8')
