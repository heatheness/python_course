# -*- coding: utf-8 -*-

u"""Реализовать класс Comparator, содержащий только поле value и метод compare, возвращающий результат сравнения value с
полем value любого другого объекта (аналогичный работе стандартной функции cmp()). Если такого поля нет, метод
возвращает 1."""

__author__ = 'nyash myash'

class Comparator (object):
    def __init__(self,value):
        self.value = value


    def compare(self,other):
        try:
            return cmp(self.value,other.value)
        except AttributeError:
            return 1


if __name__ == '__main__':
    C = Comparator(123)
    class Test: pass
    T = Test()
    T.value = 124
    print C.compare(T)