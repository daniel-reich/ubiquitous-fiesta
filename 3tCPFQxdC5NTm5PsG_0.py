
from math import sqrt
def dist(a,b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
​
from itertools import combinations
def find_triangles(lst):
    num=0
    for i in combinations(lst,3) :
        s=sorted(set((dist(i[0],i[1]),dist(i[0],i[2]),dist(i[1],i[2]))))
        if len(s)==2 and s[1]/s[0]!=2:
                num+=1
    return num

