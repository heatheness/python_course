# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

cir = list(input())
pos = list(input())
for i in xrange(0,len(pos),2):
    if not( (((pos[i])-cir[0])**2 + ((pos[i+1])-cir[1])**2) <= (cir[2])**2):
        print 'NO'
        break
else:
    print 'YES'





