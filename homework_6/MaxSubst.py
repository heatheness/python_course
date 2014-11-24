# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

s = raw_input()

max_subst = u''
b = []

for c in s:
    if c not in b:
        b.append(c)
        continue
    if len(b) > len(max_subst):
        max_subst = u''.join(b)
    b = b[b.index(c)+1:]
    b.append(c)

print max_subst if max_subst else u''.join(b)
