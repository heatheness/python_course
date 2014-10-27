# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

from decimal import *

s = raw_input().split(',')
p = [Decimal(elem) for elem in s]


v1 = [p[2]-p[0], p[3]-p[1]]
v2 = [p[6]-p[4], p[7]-p[5]]

print 'YES' if (v1[0]*v2[1] == v1[1]*v2[0]) else 'NO'


