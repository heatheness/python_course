# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

from math import *
f = raw_input()
l = [int(i) for i in raw_input().split(',')]
a = min(l)
b = max(l)
res = []

for x in xrange(a,b+1):
    try:
        res.append(eval(f))
    except:
        continue

print min(res),max(res)



