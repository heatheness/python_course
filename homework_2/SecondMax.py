# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

l = input()
if l:
    m = max(l)
    new_l = [elem for elem in l if elem < m]
    if new_l:
        print max(new_l)
    else:
        print 'NO'
else:
    print 'NO'

