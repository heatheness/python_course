# -*- coding: utf-8 -*-
"""Ввести через запятую K и N (1<N<17), вывести в столбик все K-значные N-ричные числа в порядке возрастания (латинские
буквы для цифр — большие, незначащие нули или пробелы не считаются)."""

__author__ = 'nyash myash'

from itertools import product

base = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
    16: 'G',
}

k,n = map(int, raw_input().split(','))
n_list = [base[i] for i in xrange(n)]

nums = [''.join(i) for i in product(n_list,repeat=k)]


for num in nums:
    if len(num.lstrip('0'))==k:
        print num

