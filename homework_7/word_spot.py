# -*- coding: utf-8 -*-


w = raw_input().split(' ')
l = len(w)
met = []
d = {}

for i in xrange(l):
    if w[i] in met:
        d[w[i]] = str(i)
        continue
    met.append(w[i])

string = ''
for m in met:
    if d.get(m):
        string += m + '(' + d[m] + ')' + ' '
        continue
    string += m + ' '

print string


