
tcviz
=====

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

**tcviz** is a script that can visualize your Linux traffic control (TC) configurations.
Qdiscs, classes, filters, you name it. The program has been first introduced on
[my blog](http://ze.phyr.us). Please read
[Visualizing Linux Traffic Control Setup](http://ze.phyr.us/visualizing-linux-traffic-control-setup)
for more information.


Requirements
------------

* 3.0 &le; Python
* [Graphviz](http://www.graphviz.org)

How to use
----------

`./tcviz.py eth0 | dot -Tpng > tc.png`

Examples
--------

tcviz is able to turn something like this:

	$ tc qdisc show dev eth0
	qdisc htb 1: root r2q 10 default 10 direct_packets_stat 0
	qdisc sfq 10: parent 1:10 limit 127p quantum 1514b perturb 10sec
	qdisc sfq 11: parent 1:11 limit 127p quantum 1514b perturb 10sec
	qdisc sfq 19: parent 1:19 limit 127p quantum 1514b perturb 10sec
	qdisc sfq 31: parent 1:31 limit 127p quantum 1514b perturb 10sec
	$ tc class show dev eth0
	class htb 1:11 parent 1:1 leaf 11: prio 0 rate 256000bit ceil 256000bit burst 15Kb cburst 1599b
	class htb 1:10 parent 1:1 leaf 10: prio 0 rate 128000bit ceil 128000bit burst 15Kb cburst 1599b
	class htb 1:1 root rate 10000Kbit ceil 10000Kbit burst 15Kb cburst 1600b
	class htb 1:31 parent 1:1 leaf 31: prio 0 rate 128000bit ceil 128000bit burst 15Kb cburst 1599b
	class htb 1:19 parent 1:1 leaf 19: prio 0 rate 512000bit ceil 512000bit burst 15Kb cburst 1599b
	$ tc filter show dev eth0
	filter parent 1: protocol ip pref 1 fw
	filter parent 1: protocol ip pref 1 fw handle 0x1 classid 1:11
	filter parent 1: protocol ip pref 1 fw handle 0x9 classid 1:19
	filter parent 1: protocol ip pref 1 fw handle 0x15 classid 1:31

into something like this:

![tcviz-generated graph example](https://raw.github.com/ze-phyr-us/tcviz/master/example.png)

Contributors
--------

* Stefan Forstenlechner ([t-h-e](https://github.com/t-h-e)) stefanforstenlechner@gmail.com
* [@qnnnnez](https://github.com/qnnnnez)
* [@iDawer](https://github.com/iDawer)
