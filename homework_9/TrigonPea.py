# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

import math

class Trigon (object):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        p = self.perimeter()/2.0
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

    def perimeter(self):
        return self.a+self.b+self.c

class Pea(object):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def radius(self):
        p = (self.a+self.b+self.c)/2.0
        return (self.a*self.b*self.c) / (4 * math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c)))

    def square(self):
        return math.pi * self.radius()**2

    def perimeter(self):
        return 2*math.pi * self.radius()

class TrigonPea(Trigon,Pea):
    def volume(self):
        return self.perimeter() * Pea.square(self)

if __name__ == "__main__":
    t=Trigon(3,4,5)
    p=Pea(3,4,5)
    z=TrigonPea(3,4,5)
    print "{:.6f}".format(t.square())
    print "{:.6f}".format(t.perimeter())
    print "{:.6f}".format(p.square())
    # print "{:.6f}".format(p.perimeter())
    print "{:.6f}".format(z.volume())
    print "{:.6f}".format(z.square())
    # print "{:.6f}".format(z.perimeter())


