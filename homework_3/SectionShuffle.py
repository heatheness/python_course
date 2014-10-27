# -*- coding: utf-8 -*-

__author__ = 'nyash myash'


s = input()
l = len(s)

u = [s[i] for i in reversed(xrange(0,l,2))]
w = [s[i] for i in xrange(1,l,2)]

u.extend(w)
print tuple(u)
