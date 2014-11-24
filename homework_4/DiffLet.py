# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

def func(s):
    return len(set(s))

# s = raw_input()
# s = s.split()

s = 'aaa b a cc wwwww eee  yui  abaaaaabbbbbab vnvv fgfgfgfg werwerwer axaxxxxxaxaxaxaxaxx'
# s = s.rsplit()
# print s


p = sorted(s.split(),key = lambda x: len(set(x)))
e = " ".join(p)

print e

