# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

import random

def gen_lab(m):
    """генерирует лабиринт"""

    def lab_to_string(lab):
        """преобразует лабиринт (лист листов) в строку"""
        s = ''
        for i in lab:
            s = s + ''.join(i) + '\n'
        return s

    def gen_filed(m):
        """генерирует поле точек размером m x m"""
        l = [ ['.'] *m for i in xrange(m)]
        return l


    def gen_route(l):
        """генерирует случайный мрашрут"""
        n = len(l)-1
        visited = []
        route = []
        plan = [[(0,0),None]]

        while True:
            cur = plan.pop()
            # print cur
            # print 'cur ',cur
            directs = []
            if cur[0] in visited:
                continue
            elif cur[0] == (n,n):
                break
            else:
                route.append(cur[0])
                visited.append(cur[0])
                i,j = cur[0]
                # print 'i,j', i,j
                if (j-1) >= 0 and ((i,j-1) not in visited):
                    directs.append([(i,j-1),cur[0]])
                    # print i,j
                    # print 'left appended', directs
                if (i+1) <= n and ((i+1,j) not in visited):
                    directs.append([(i+1,j),cur[0]])
                    # print i,j
                    # print 'down appended', directs
                if (j+1) <= n and ((i,j+1) not in visited):
                    directs.append([(i,j+1),cur[0]])
                    # print i, j
                    # print 'right appended', directs
                if (i-1) >= 0 and ((i-1,j)not in visited):
                    directs.append([(i-1,j),cur[0]])
                    # print i,j
                    # print 'up appended', directs
                # print 'directs ',directs
                if not directs:
                    route.pop()
                    new_cur_par = plan[-1][1]
                    while True:
                        if route[-1] != new_cur_par:
                            route.pop()
                        else:
                            break
                    continue
                else:
                    random.shuffle(directs)
                    # print 'shuffled directs', directs
                    plan.extend(directs)
        route.append((n,n))
        return route


    def gen_walls(l, route):
        """генерирует стены в лабиринте"""
        w = len(l)
        # вероятность построения стен зависит от отношения длины пути к размеру лабиринта
        # чем больше путь, тем больше вероятность, что на свободных местах появятся стены
        if w <5:
            p = 8
        else:
            p = int(len(route)*10.0/w**2)
        if p < 4: p = 4 # корректировка, чтобы не было совсем пусто
        for i in xrange(m):
            for j in xrange(m):
                if (i,j) not in route:
                    key = random.randint(0,11)
                    if key <= p:
                        l[i][j]='#'



    l = gen_filed(m)

    while True:
        way = gen_route(l)
        w = len(way)
        if (w != m**2) or (w==1) :
            break

    gen_walls(l,way)

    return lab_to_string(l)



m = int(raw_input())
s = gen_lab(m)
print s









