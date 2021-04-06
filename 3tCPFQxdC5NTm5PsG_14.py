
from itertools import combinations as C
def coline(a,b,c):
  return (b[1]-a[1])*(c[0]-a[0])==(c[1]-a[1])*(b[0]-a[0])
def dist(a,b):
  return ((a[0]-b[0])**2+(a[1]-b[1])**2)**.5
def find_triangles(lst):
  count=0
  for a,b,c in C(lst,3):
    if not coline(a,b,c):
      if dist(a,b)==dist(b,c) or dist(a,b)==dist(a,c) or dist(a,c)==dist(b,c):
        count+=1
  return count

