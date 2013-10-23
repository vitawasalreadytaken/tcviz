# tcviz 1.2
#
# $Id: Filter.py 41 2009-12-28 19:37:51Z zephyr $
#
# Licensed under the terms of the MIT/X11 license.
# Copyright (c) 2009 Vita Smid <me@ze.phyr.us>


import textwrap
from Id import Id

class Filter:
	COLOR = '#999999'


	def __init__(self, spec = None):
		self.__parent = None
		self.__target = None
		self.__params = []

		if spec is not None:
			self.parseSpec(spec)


	def parseSpec(self, spec):
		spec = spec.split(' ')[2:]
		self.__parent = Id(spec.pop(0))

		while spec:
			item = spec.pop(0)
			if item == 'classid' or item == 'flowid':
				self.__target = Id(spec.pop(0))
			else:
				self.__params.append(item)


	def getEdgeSpec(self):
		if self.__target is None:
			return ''
		label = '<br/>'.join(textwrap.wrap(' '.join(self.__params), 20))
		fmt = '"%s" -> "%s" [ arrowhead = "vee", color = "%s", label = <<font point-size="10" color="%s">%s</font>>, style = "dotted" ];'
		return fmt % (self.__parent, self.__target, self.COLOR, self.COLOR, label)
