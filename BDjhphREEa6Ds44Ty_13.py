
import math
def bomb(lst):
    distance = lambda x1, y1, x2, y2: math.sqrt((x1-x2)**2+(y1-y2)**2)
    for i in lst: i[2]=round(i[2]*0.343)
    lol1, lol2, lol3 = [], [], []
    p1, p2, p3 = [], [], []
    for i in range(51):
        for j in range(51):
            lol1.append([j, i]) if round(distance(j, i, lst[0][0], lst[0][1])) == lst[0][2] else 0
            lol2.append([j, i]) if round(distance(j, i, lst[1][0], lst[1][1])) == lst[1][2] else 0
            lol3.append([j, i]) if round(distance(j, i, lst[2][0], lst[2][1])) == lst[2][2] else 0
​
    [p1.append(i) for i in lol1 if i not in p1]
    [p2.append(i) for i in lol2 if i not in p2]
    [p3.append(i) for i in lol3 if i not in p3]
    return tuple([i for i in p1 if i in p2 and i in p3][-1])

