
from itertools import combinations
def is_parallelogram(lst):
  m=[slope(*i) for i in combinations(lst,2)]
  return len(m)-len(set(m))==2
  
def slope(a,b):
  try:return (b[0]-a[0])/(b[1]-a[1])
  except:return 'inf'

