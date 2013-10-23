# tcviz 1.2
#
# $Id: Id.py 44 2012-10-08 09:32:14Z zephyr $
#
# Licensed under the terms of the MIT/X11 license.
# Copyright (c) 2012 Vita Smid <me@ze.phyr.us>


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

