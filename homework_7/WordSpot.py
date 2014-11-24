# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

words = raw_input().split()
reversed = words[:]
reversed.reverse()

print words
print reversed

l = len(words)
s = ""
for i,w  in enumerate(words):
    j = reversed.index(w)
    k = l-j-1
    if i != k:
        s+= w + "(" + str(k) + ") "
    else:
        s+= w





