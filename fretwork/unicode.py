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


def unicodify(s):
    """Return a unicode string"""
    if isinstance(s, bytes):
        return s.decode('utf-8')

    return str(s)


def utf8(s):
    """Return a valid UTF-8 bytestring"""
    return unicodify(s).encode("utf-8")
