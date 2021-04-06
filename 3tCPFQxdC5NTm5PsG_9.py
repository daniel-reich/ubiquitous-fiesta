
import itertools
import math
​
def get_sq_distance(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
​
def find_triangles(lst):
    ans = 0
    for comb in itertools.combinations(lst, 3):
        p1, p2, p3 = comb
        v1 = [p1[0] - p2[0], p1[1] - p2[1]]
        v2 = [p3[1] - p1[1], p3[0] - p1[0]]
        dists = [get_sq_distance(p1, p2), get_sq_distance(p2, p3), get_sq_distance(p1, p3)]
        a, b, c = [math.sqrt(d) for d in dists        ]
        if len(set(dists)) < 3 and \
           a+b > c and b+c > a and a+c >b:
            ans += 1
    return ans

