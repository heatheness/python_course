# -*- coding: utf-8 -*-

__author__ = 'mayns'


n = int(raw_input())
l = raw_input()
l = map(int, l.split(u','))


def summer(k, s):
    if s:
        m = s.pop()
        if k - m in s:
            return True
        return summer(k - m, [i for i in s if i <= k - m])
    return False


def sum_checker(k, s):
    if k in s:
        return u'YES'
    if k > sum(s):
        return u'NO'
    s = sorted([i for i in s if i < k])
    check_ok = False
    sl = len(s)
    for c in reversed(range(sl)):
        slices = s[:c+1]
        check_ok = summer(k, slices)
        if check_ok:
            break
        if not slices:
            break
        slices.pop()
    return u'YES' if check_ok else u'NO'

print sum_checker(n, l)
