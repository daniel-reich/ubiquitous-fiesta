
from itertools import combinations
​
def is_iso(t):
    d, ang, comb, p1, p2 = [0, 0, 0], [0, 0], [[0,1],[1,2],[0,2]], 0, 0
    for i in comb:
        d[p1] = (t[i[0]][0]-t[i[1]][0])**2+(t[i[0]][1]-t[i[1]][1])**2
        p1 += 1
    if any(d[i[0]] == d[i[1]] for i in comb):
        for j in comb[:2]:
            if t[j[0]][0] == t[j[1]][0]: ang[p2] = float('inf')
            else: ang[p2] = (t[j[0]][1]-t[j[1]][1])/(t[j[0]][0]-t[j[1]][0])
            p2 += 1
    return ang[1] != ang[0]
​
def find_triangles(lst):
    comb, soma = combinations(range(len(lst)), 3), 0
    for i in comb: soma += is_iso([lst[i[0]], lst[i[1]], lst[i[2]]])
    return soma

