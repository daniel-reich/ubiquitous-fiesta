
from itertools import combinations
def find_triangles(lst):
  ret = []
  for c in combinations(lst,3):
    temp = [list(i) for i in list(c)]
    x1,y1 = temp[0]
    x2,y2 = temp[1]
    x3,y3 = temp[2]
    if len(set([dist(x1,y1,x2,y2),dist(x1,y1,x3,y3),dist(x2,y2,x3,y3)]))==2:
      if len(set([slope(x1,y1,x2,y2),slope(x1,y1,x3,y3),slope(x2,y2,x3,y3)]))==3:
        if temp not in ret: 
          ret.append(temp)
  return len(ret)
  
def dist(x1,y1,x2,y2):
  return ((x2-x1)**2+(y2-y1)**2)**(1/2)
​
def slope(x1,y1,x2,y2):
  return (y2-y1)/(x2-x1) if x2-x1!=0 else None

