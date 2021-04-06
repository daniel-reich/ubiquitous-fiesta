
def advanced_sort(lst):
  unique, l =  [], []
  for e in lst:
    if e not in unique:
      l.append([e] * lst.count(e))
      unique.append(e)
  return l

