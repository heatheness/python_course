# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

# m,n = raw_input().split(',')
# m = int(m)
# n = int(n)
#
# v = str(m)
# res = m*n
# l_s = len(str(res)+'_=_'+str(n) + '_*_' + v) # определеям длину максимальной строки в таблице
# # print str(res)+'_=_'+str(n) + '_*_' + v
# # print l_s
# l_m = len(str(m)) # запоминаем длину m, чтобы сто раз не считать
# l_res = len(str(res))  # запоминаем длину  максимального результата
# for i in xrange(1,n+1):
#     p = str(i*m)
#     k = str(i)
#     d = l_s - (len(p)+len(k) + l_m + 6) # разница между длиной максимальной строки и текущей
#     if d==0:
#         pass
#     else:
#         g = l_res - len(p)  #  разница длин результатов
#         if g:
#             p = '_'*g + p  # выравниваем длины результатов счет _ перед p
#         j = d-g
#         if j:
#             k = '_'*j + k # выравниваем оставшееся за счет _ перед k
#     print p + '_=_' + k + '_*_' + v



inpt = input()
m = inpt[0]
n = inpt[1]
max_len = len(str(m*n))

for i in range(1, n + 1):
    print '{2:_>{3}}_=_{1:_>{4}}_*_{0}'.format(m,i,m*i, max_len, len(str(n)));

