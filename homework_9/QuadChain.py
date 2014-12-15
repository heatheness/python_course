# -*- coding: utf-8 -*-

def is_sum(s,i,l):
    j = i+1
    w = len(l)
    while True:
        q = sum(l[i:j])
        if s == q:
            return j
        if j>=w or q > s:
            return None
        j+=1

l = [int (i) for i in raw_input().split(',')]
# l = [1, 3, 2, 2, 4, 5]
p = sum(l)/2
i = 1
u = len(l)
while True:
    # print 'i is ', i
    a = sum(l[:i])
    # print 'a is ', a
    b = p - a
    if a==0 or b ==0:
        i+=1
        continue
    if i > u-3:
        print 'NO'
        break
    j = is_sum(b,i,l)
    # print 'current j ',j
    if not j:
        i +=1
        continue
    j = is_sum(a,j,l)
    # print 'current j ',j
    if not j:
        i+=1
        continue
    j = is_sum(b,j,l)
    # print 'current j ',j
    if not j:
        i+=1
        continue
    elif not l[j:]:
        print 'YES'
        break
    else:
        i+=1
        continue

