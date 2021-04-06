
def alternate_sort(lst):
  a = sorted([c for c in lst if type(c)==str])
  n = sorted([b for b in lst if type(b)==int])
  r = []
  for i, x in enumerate(a):
    r.append(n[i])
    r.append(a[i])
  return r

