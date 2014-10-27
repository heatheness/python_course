# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

from collections import defaultdict

u = []
while True:
    w = raw_input()
    if w:
        u.extend(w.rsplit())
    else:
        break

d = defaultdict(int)
for i in u:
    d[i] +=1

l = sorted(d.keys(),cmp=None, key= lambda x: d[x], reverse = True)

if len(l) >1 and d[l[0]] == d[l[1]]:
    print '---'
else:
    print l[0]





