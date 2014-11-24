# -*- coding: utf-8 -*-

__author__ = 'nyash myash'


class Vovel(object):
    def __getattr__(self, item):
        vowels = set("aeiou")
        atr = str(item)
        s = set(atr)
        if s.difference(vowels):
            raise AttributeError("Vovel instance has no attribute '{}'".format(atr))
        else:
            return atr.upper()

if __name__=="__main__":
    A = Vovel()
    print A.aoao
    try:
        print A.field
    except AttributeError, msg:
        print "ERROR",msg