
from itertools import combinations
​
def find_triangles(lst):
    triangles = 0
    for (x1, y1), (x2, y2), (x3, y3) in combinations(lst, 3):
        a = round(((x1-x2)**2 + (y1-y2)**2)**0.5, 2)
        b = round(((x1-x3)**2 + (y1-y3)**2)**0.5, 2)
        c = round(((x2-x3)**2 + (y2-y3)**2)**0.5, 2)
        collinear = 0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) == 0
        if (a == b or b == c or a == c) and not collinear:
            triangles += 1
    return triangles

