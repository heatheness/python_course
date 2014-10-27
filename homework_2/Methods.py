# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

obj = input()
for method in dir(obj):
    if method[0]!='_':
        print method