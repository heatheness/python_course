# -*- coding: utf-8 -*-

__author__ = 'nyash myash'


l = [int(i) for i in raw_input().split(',')]
y = int(raw_input())
x,a,c,m = l


for i in xrange(m):
    x = (a*x + c) % m
    if y == x:
        print 'YES'
        break
else:
    print 'NO'


