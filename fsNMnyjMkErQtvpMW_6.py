
def holey_sort(lst):
  import operator
  h = ['0','4','6','8','9']
  n = [sum([2 if i=='8' else 1 if i in h else 0 for i in str(x)]) for x in lst]
  z = [x for x in zip(lst,n)]
  l = []
  if set(n)!=len(lst):
    for y in range(max(n)+1):
      for k,v in z:
        if v==y:  l.append(k)
  return l

