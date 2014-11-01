# -*- coding: utf-8 -*-

__author__ = 'nyash myash'


l = raw_input().split(' ')
stack = []
operations = '+-*/'

try:
    for element in l:
        if element not in operations:
            stack.append(element)
        else:
            b = stack.pop()
            a = stack.pop()
            c = eval(a+element+b)
            stack.append(str(c))
except:
    print 'ERROR'
else:
    if len(stack) == 1:
        print stack[0]
    else:
        print 'ERROR'




