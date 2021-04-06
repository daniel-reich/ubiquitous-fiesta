
def alternate_sort(lst):
  l = sorted([x for x in lst if isinstance(x,str)])
  d = sorted([x for x in lst if isinstance(x,int)])
  return  sum([list(x) for x in zip(d,l)],[])

