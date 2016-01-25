"""Generates random (x,y,theta) tuples"""
from random import randint
import sys
for i in xrange(int(sys.argv[1])):
	print str(randint(-180,180))+'\t'+str(randint(-180,180))+'\t'+str(randint(0,360))