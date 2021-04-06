
from itertools import combinations
​
​
def distance_pow2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
​
​
def find_triangles(lst):
    count = 0
    for comb in combinations(lst, 3):
        edges = [distance_pow2(*edge) for edge in combinations(comb, 2)]
        if len(set(edges)) == 2:
            a, b = 0, 0
            for x in set(edges):
                if edges.count(x) == 2:
                    a = x
                elif edges.count(x) == 1:
                    b = x
            if 2 * (a ** 0.5) > b ** 0.5:
                count += 1
    return count

