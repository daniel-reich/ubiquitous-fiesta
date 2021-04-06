
from itertools import permutations
def is_parallelogram(lst):
  lst = [list(i) for i in lst]
  perm = [list(p) for p in permutations(lst,2)]
  slopes = [slope(i) for i in perm]
  slopes = [str(i) for i in slopes if i!=None]
  slopes = list(set(slopes))
  return len(slopes)<=4
  
def slope(lst):
  x1,y1 = lst[0]
  x2,y2 = lst[1]
  return (y2-y1)/(x2-x1) if (x2-x1)!=0 else None

