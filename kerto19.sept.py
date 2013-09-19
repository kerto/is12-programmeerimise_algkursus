#!/usr/bin/python

from random import randint

for n in xrange(15):
	kuulid = ["s"]*5+["m"]*10+["v"]*15
	print kuulid[randint(0,29)]

for n in kuulid(10):
	print n











