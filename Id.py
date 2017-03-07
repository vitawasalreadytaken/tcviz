# tcviz 1.2
#
# Licensed under the terms of the MIT/X11 license.
# Copyright (c) 2009-2013 Vita Smid <http://ze.phyr.us>


class Id:
    def __init__(self, spec='1:0'):
        (self._major, self._minor) = spec.split(':')

    def __str__(self):
        return '%s:%s' % (self._major, self._minor)

    __unicode__ = __repr__ = __str__
