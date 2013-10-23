#!/usr/bin/env python

# tcviz 1.2
#
# Licensed under the terms of the MIT/X11 license.
# Copyright (c) 2009-2013 Vita Smid <http://ze.phyr.us>


import subprocess, sys
from Node import Node
from Filter import Filter

TCPATH = '/sbin/tc'

def main():
	if len(sys.argv) == 2:
		(q, c, f) = [ readTc([type, 'show', 'dev', sys.argv[1]]) for type in ('qdisc', 'class', 'filter') ]
	elif len(sys.argv) == 4:
		(q, c, f) = [ readFile(p) for p in sys.argv[1:4] ]
	else:
		usage()
		return 1

	nodes = parse(q, Node) + parse(c, Node)
	filters = parse(f, Filter)

	gv = 'digraph tc { %s \n %s \n %s \n %s }' % (genSetup(), genNodes(nodes), genEdges(nodes), genEdges(filters))
	print gv
	return 0


def usage():
	print >>sys.stderr, 'Usage: %s <interface>' % sys.argv[0]
	print >>sys.stderr, '\nOR'
	print >>sys.stderr, 'If you want to feed tcviz with offline data:'
	print >>sys.stderr, '%s <qdiscs file> <classes file> <filters file>' % sys.argv[0]


def readFile(path):
	return open(path).read()


def readTc(args):
	return subprocess.Popen([TCPATH] + args, stdout = subprocess.PIPE).communicate()[0]


def parse(string, constructor):
	specs = []
	for line in string.split('\n'):
		if not line:
			continue
		elif line[:2] == '  ': # continuation of the previous line
			specs[-1] += ' ' + line.strip()
		else:
			specs.append(line.strip())
	return [ constructor(spec) for spec in specs ]


def genSetup():
	return 'node [ fontname = "DejaVu Sans" ]; edge [ fontname = "DejaVu Sans" ];'


def genNodes(objects):
	return '\n'.join([ o.getNodeSpec() for o in objects ])


def genEdges(objects):
	return '\n'.join([ o.getEdgeSpec() for o in objects ])


if __name__ == '__main__':
	sys.exit(main())
