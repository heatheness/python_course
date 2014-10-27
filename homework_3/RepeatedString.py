# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

# import timeit

s = raw_input()

# s = 'abcthukijlinuybert'*100000000
# start = timeit.default_timer()
l = len(s)


d = (x for x in xrange(1,l/2+1) if l/x == float(l)/x)

for i in d:
    t = s[:i]
    k = s.count(t)
    if i*k == l:
        print k
        break
else:
    print 1


# print timeit.default_timer()-start


