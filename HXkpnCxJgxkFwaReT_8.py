
from collections import OrderedDict
​
def count_datatypes(*args):
  
  counts = [0,0,0,0,0,0]
  l = [int, str, bool, list, tuple, dict]
  counts = [0,0,0,0,0,0]
  for i in args:
    if type(i) in l:
      counts[l.index(type(i))]+=1
  return counts

