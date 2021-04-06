
from itertools import combinations
def distance (tup1,tup2):
  return ((tup1[0]-tup2[0])**2 + (tup1[1]-tup2[1])**2)**.5
def find_triangles(lst):
  lst1,counter,keep=list(combinations(lst,3)),0,[]
  for k in range (len(lst1)):
    dist=[]
    for i in range (len(lst1[k])-1):
      for j in range(i+1,len(lst1[k])):
        dist.append(distance(lst1[k][i],lst1[k][j]))
    if len(dist)-len(set(dist))==1  and max(dist) < (sum([d for d in dist])-max(dist)) and lst1[k] not in keep:
      counter+=1
      keep.append(lst1[k])
  return counter

