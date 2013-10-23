# tcviz 1.2
#
# Licensed under the terms of the MIT/X11 license.
# Copyright (c) 2009-2013 Vita Smid <http://ze.phyr.us>


class Id:
	def __init__(self, spec = '1:0'):
		(self.__major, self.__minor) = map(self.__parseId, spec.split(':'))


	def __parseId(self, id):
		'''Parse a major or minor number.'''
		if not id:
			return 0
		else:
			return int(id, 16)


	def __str__(self):
		return '%x:%x' % (self.__major, self.__minor)


	__unicode__ = __repr__ = __str__

