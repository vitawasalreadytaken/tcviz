#!/usr/bin/env python3

# tcviz 1.2
#
# Licensed under the terms of the MIT/X11 license.
# Copyright (c) 2009-2013 Vita Smid <http://ze.phyr.us>


import subprocess
import sys
from itertools import chain

from Filter import Filter
from Node import Node

TCPATH = '/sbin/tc'


def main():
    f = ''
    if len(sys.argv) == 2:
        (q, c) = [readTc([type, 'show', 'dev', sys.argv[1]]) for type in ('qdisc', 'class')]
    elif len(sys.argv) == 4:
        (q, c, f) = [readFile(p) for p in sys.argv[1:4]]
    else:
        usage()
        return 1

    qdiscs = parse(q, Node)
    classes = parse(c, Node)

    if len(sys.argv) == 2:
        f = '\n'.join([readTc(['filter', 'show', 'dev', sys.argv[1], 'parent', str(cur._id)]).replace('filter', 'filter parent {}'.format(cur._id)) for cur in chain(qdiscs, classes)])

    filters = parse(f, Filter)

    nodes = qdiscs + classes
    gv = 'digraph tc { %s \n %s \n %s \n %s }' % (genSetup(), genNodes(nodes), genEdges(nodes), genEdges(filters))
    print(gv)
    return 0


def usage():
    print('Usage: %s <interface>' % sys.argv[0], file=sys.stderr)
    print('\nOR', file=sys.stderr)
    print('If you want to feed tcviz with offline data:', file=sys.stderr)
    print('%s <qdiscs file> <classes file> <filters file>' % sys.argv[0], file=sys.stderr)


def readFile(path):
    return open(path).read()


def readTc(args):
    return subprocess.Popen([TCPATH] + args, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]


def parse(string, constructor):
    specs = []
    for line in string.split('\n'):
        if not line:
            continue
        elif line.startswith(' ') or line.startswith('\t'):  # continuation of the previous line
            specs[-1] += ' ' + line.strip()
        else:
            specs.append(line.strip())
    return [constructor(spec) for spec in specs]


def genSetup():
    return 'node [ fontname = "DejaVu Sans" ]; edge [ fontname = "DejaVu Sans" ];'


def genNodes(objects):
    return '\n'.join([o.getNodeSpec() for o in objects])


def genEdges(objects):
    return '\n'.join([o.getEdgeSpec() for o in objects])


if __name__ == '__main__':
    sys.exit(main())
