
def alternate_sort(lst):
  a = sorted([x for x in lst if type(x)!= int])
  d = sorted([x for x in lst if type(x)== int])
  res = []
  for x in range(len(a)):
    res.append(d[x])
    res.append(a[x])
  return res

