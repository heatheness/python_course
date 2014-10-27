# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

def func(s):
    return len(set(s))

# s = raw_input()
# s = s.rsplit()

s = 'aaa b a cc wwwww eee   abaaaaabbbbbab vnvv fgfgfgfg werwerwer axaxxxxxaxaxaxaxaxx'
s = s.rsplit()
# print s

d = dict()
for i in s:
    num_of_sym = func(i)
    if num_of_sym:
        if num_of_sym not in d:
            d[num_of_sym] = []
            d[num_of_sym].append(i)
        else:
            d[num_of_sym].append(i)


e = ''
for i in sorted(d.keys()):
    for string in d[i]:
        e = e+string+' '

print e
