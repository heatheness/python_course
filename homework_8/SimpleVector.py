# -*- coding: utf-8 -*-

u""""Реализовать класс Vector, позволяющий
- задавать двумерный вектор (из двух чисел)
- вычислять вектор — сумму двух векторов
- вычислять вектор — результат умножения вектора на число (или числа на вектор)
- скалярно умножать вектор на вектор
- преобразовывать вектор в строку вида |x,y|"""

__author__ = 'nyash myash'


class Vector(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self,other):
        if isinstance(self, Vector) and isinstance(other, Vector):
            return self.x*other.x + self.y*other.y
        elif isinstance(other,int):
            return Vector(self.x * other, self.y * other)
        else:
            Vector.__rmul__(self,other)

    def __rmul__(self,other):
        return Vector(self.x * other, self.y * other)


    def __str__(self):
        return "|{},{}|".format(self.x, self.y)

if __name__ == "__main__":
    A = Vector(1,2)
    B = Vector(3,4)
    print A
    print A+B
    print A*B
    print 7*A
    print A*7