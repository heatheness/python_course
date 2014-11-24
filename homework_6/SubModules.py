# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

import types

module = raw_input()

try:
    imported = __import__(module)
    counter = 0
    for item in dir(imported):
        attr = getattr(imported,item)
        if isinstance(attr,types.ModuleType): counter+=1
    print counter
except ImportError:
    print -1


# try:
#     module = __import__(mod)
#     dirs = dir(module)
#     counter = [m for m in dirs if type(getattr(module, m)) == type(module)]
#     print len(counter)
# except ImportError:
#     print -1