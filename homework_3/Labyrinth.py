# -*- coding: utf-8 -*-

__author__ = 'nyash myash'


s = raw_input()
l = []
l.append(list(s))
n = len(s) - 1

for i in xrange(n):
    s = raw_input()
    l.append(list(s))

# l = ['.....',
#      '#.#.#',
#      '....#',
#      '..##.',
#      '.....']

# n = len(l[0]) - 1
# # print l
# # print n

plan = [(0,0)]
visited = []
i = 0
j = 0
if l[n][n] == '#':
    print 'NO'
else:
    while True:
        if (j-1) >= 0 and (i,j-1) and l[i][j-1]!='#' and (i,j-1) not in visited:
            plan.append((i,j-1))
        if (i+1) <= n and l[i+1][j]!='#' and (i+1,j) not in visited:
            plan.append((i+1,j))
        if (j+1) <= n and l[i][j+1]!='#' and (i,j+1) not in visited:
            plan.append((i,j+1))
        if (i-1) >= 0 and l[i-1][j]!='#' and (i-1,j) not in visited:
            plan.append((i-1,j))
        cur = plan.pop()
        visited.append(cur)
        # print cur
        i,j = cur
        if cur == (n,n):
            print 'YES'
            break
        if plan == []:
            print 'NO'
            break







