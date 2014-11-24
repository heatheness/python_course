# -*- coding: utf-8 -*-

u"""Реализовать клаcc Dot, позволяющий:
- Задавать точку в N-мерном пространстве (с помощью N чисел, где N>0)
- Преобразовывать точку в строку вида «X1,X2,…,XN»
- Вычислять расстояние (distance()) между двумя точками пространства одинаковой размерности
- Вычислять точку (middle()) — середину отрезка между двумя точками пространства одинаковой размерности
- При попытке работы с такими же точками пространства, но разной размерности порождать исключение ValueError"""

__author__ = 'nyash myash'



class Dot (object):
    def __init__(self,*args):
        self.coordinate = args

    def __str__(self):
        return ",".join(map(str,self.coordinate))

    def check_dim(self,other):
        if len(self.coordinate) != len(other.coordinate):
            raise ValueError

    def distance(self,other):
        self.check_dim(other)
        return (sum([(a-b)**2  for a,b in zip(self.coordinate, other.coordinate)]))**0.5

    def middle (self,other):
        self.check_dim(other)
        return Dot(*[(a+b)/2.0  for a,b in zip(self.coordinate, other.coordinate)])

if __name__ == "__main__":
    for A,B in (Dot(1,2,3),Dot(3,4,5)), (Dot(1,2),Dot(3)):
        print A
        try:
            print "{:.3f}".format(A.distance(B))
            print A.middle(B)
        except ValueError:
            print "ERROR"