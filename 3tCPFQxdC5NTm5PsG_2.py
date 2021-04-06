
import numpy as np
from itertools import combinations
​
def slope(p1,p2):
    if p2[0]==p1[0]: return 'inf'
    return (p2[1]-p1[1])/(p2[0]-p1[0])
​
def istri(lst):
    return len({slope(lst[0],lst[1]), slope(lst[1],lst[2]), slope(lst[2],lst[0])}) == 3
​
def sqdist(p1, p2):
    return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
​
def isiso(lst):
    return len({sqdist(lst[0],lst[1]),sqdist(lst[1],lst[2]),sqdist(lst[2],lst[0])}) < 3
def find_triangles(lst):
    return sum(map(lambda x: isiso(x) and istri(x),combinations(lst,3)))

