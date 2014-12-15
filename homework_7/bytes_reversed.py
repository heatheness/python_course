# -*- coding: utf-8 -*-

import struct


w = raw_input()
w = map(int, w.split(u','))
key = struct.pack(len(w)*'l', *w)
val = struct.unpack(len(w)*'l', key[::-1])
print list(val)