# -*- coding: utf-8 -*-

__author__ = 'nyash myash'


import timeit

# n = int(raw_input())
# l = raw_input().split(',')

# n = 1219
# # l =[1,4,3,1,14,16,12,11,19,90,21,10,16,18,19,40,80,300,21,22,500,10,680,780,800,7000,9090,8907,7656,10000]
# start = timeit.default_timer()
#
# l = ['1','2','3','4','5','10','31','12','23','40','14','20','90']
# l = [i for i in l if i <=n]
# l.sort()
# l = [int(i) for i in l if int(i) <=n]
#
#
#
# # u = 0
# def pack(l, i, s):
#     # global u
#     # u +=1
#     # print u
#     if i >= len(l): return 1 if s == 0 else 0
#     count = pack(l, i + 1, s)
#     if count: return 1
#     count += pack(l, i + 1, s - l[i])
#     return count
#
# #[2,3,8,9,11]
# if n in l:
#     print 'YES'
# # elif n > sum(l):
# #     print 'NO'
# else:
#     print 'YES' if pack(l,0, n) else 'NO'
#
#
# print timeit.default_timer() - start
#
l = [2,3,8,9,11]
l.reverse()
n = 21

def smart_pop(summae,elems):
    if summae == n:
        return True
    elif len(elems) > 0 and summae < n:
        for i in range(0,len(elems)):
            new_elems = elems[:]
            elem = new_elems.pop(i)
            if smart_pop(summae+elem,new_elems):
                return True

print "YES" if smart_pop(0, l) else "NO"