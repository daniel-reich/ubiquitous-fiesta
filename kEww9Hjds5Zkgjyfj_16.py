
def replace_next_largest(lst):
  ls = sorted(lst)
  k = []
  m = max(lst)
  for i in lst:
    if i == m:
      k.append(-1)
    else:
      k.append(ls[ls.index(i) + 1])
  return k

