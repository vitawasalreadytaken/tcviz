# tcviz 1.2
#
# Licensed under the terms of the MIT/X11 license.
# Copyright (c) 2009-2013 Vita Smid <http://ze.phyr.us>


import textwrap

from Filter import Filter
from Id import Id


class Node:
    def __init__(self, spec=None):
        self._id = None
        self._nodeType = None
        self._parent = None
        self._type = None
        self._params = []

        if spec is not None:
            self.parseSpec(spec)

    def parseSpec(self, spec):
        spec = spec.split(' ')
        self._nodeType = spec.pop(0)
        self._type = spec.pop(0)
        self._id = Id(spec.pop(0))
        if spec.pop(0) == 'parent':
            self._parent = Id(spec.pop(0))
        else:
            self._parent = Id("{}:".format(self._id._major)) if self._nodeType == 'class' else None

        self._params = self._filterParams(spec)

    def _filterParams(self, spec):
        params = []
        while spec:
            item = spec.pop(0)
            if item == 'leaf':  # remove unwanted "leaf" specs
                spec.pop(0)
            else:
                params.append(item)
        return params

    def getParent(self):
        return self._parent

    def getNodeSpec(self):
        desc = '<br/>'.join(textwrap.wrap(' '.join(self._params), 30)) or ' '
        label = '<font color="blue">%s</font><br/>%s<br/><font point-size="10">%s</font>' % (
        self._id, self._type, desc)
        shape = 'box' if self._nodeType == 'qdisc' else 'ellipse'
        return '"%s" [ label = <%s>, shape = "%s" ];' % (self._id, label, shape)

    def getEdgeSpec(self):
        ret = ''
        if self._parent:
            ret = '"%s" -> "%s" [ arrowhead = "none", arrowtail = "normal", dir = "both"];' % (self._parent, self._id)

        if self._nodeType == 'qdisc' and 'default' in self._params:
            dcls_minor = self._params[self._params.index('default') + 1].lstrip('0x')
            ret += '\n' + Filter('  {0}: default classid {0}:{1}'.format(self._id._major, dcls_minor)).getEdgeSpec()
        return ret
