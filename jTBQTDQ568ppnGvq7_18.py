
import itertools
​
def digit_sort(lst):
  lst=[str(x) for x in lst]
  lst.sort(key=len,reverse=True)
  res=[]
  for k,g in itertools.groupby(lst,key=len):
    for x in sorted(g):
      res.append(int(x))
  return res

