# tcviz 1.2
#
# Licensed under the terms of the MIT/X11 license.
# Copyright (c) 2009-2013 Vita Smid <http://ze.phyr.us>


import textwrap
from Id import Id


class Node:
	def __init__(self, spec = None):
		self.__id = None
		self.__nodeType = None
		self.__parent = None
		self.__type = None
		self.__params = []

		if spec is not None:
			self.parseSpec(spec)


	def parseSpec(self, spec):
		spec = spec.split(' ')
		self.__nodeType = spec.pop(0)
		self.__type = spec.pop(0)
		self.__id = Id(spec.pop(0))
		if spec.pop(0) == 'parent':
			self.__parent = Id(spec.pop(0))
		else:
			self.__parent = Id() if self.__nodeType == 'class' else None

		self.__params = self.__filterParams(spec)


	def __filterParams(self, spec):
		spec = filter(None, spec)
		params = []
		while spec:
			item = spec.pop(0)
			if item == 'leaf': # remove unwanted "leaf" specs
				spec.pop(0)
			else:
				params.append(item)
		return params


	def getParent(self):
		return self.__parent


	def getNodeSpec(self):
		desc = '<br/>'.join(textwrap.wrap(' '.join(self.__params), 30)) or ' '
		label = '<font color="blue">%s</font><br/>%s<br/><font point-size="10">%s</font>' % (self.__id, self.__type, desc)
		shape = 'box' if self.__nodeType == 'qdisc' else 'ellipse'
		return '"%s" [ label = <%s>, shape = "%s" ];' % (self.__id, label, shape)


	def getEdgeSpec(self):
		if self.__parent is None:
			return ''
		return '"%s" -> "%s" [ arrowhead = "none", arrowtail = "normal"];' % (self.__parent, self.__id)
