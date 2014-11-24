# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

from itertools import product

numbers = raw_input()
numbers = numbers.split(u' ')
complexity = len(numbers)
signs = [u'+', u'-']

combs = list(product(signs, repeat=complexity-2))

enough = 0

for comb in combs:
    for i, number in enumerate(numbers[:-1]):
        c = list(comb[:])
        c.insert(i, u'==')
        equation = u''.join(reduce(lambda x, y: x + y, zip(numbers, c))) + numbers[-1]
        if eval(equation):
            print u'YES'
            enough = 1
            break
    if enough:
        break
else:
    print u'NO'