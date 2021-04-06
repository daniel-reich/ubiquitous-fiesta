
def advanced_sort(lst):
  out, seen = [], []
  for x in lst:
    if x not in seen:
      out.append([x] * lst.count(x))
      seen.append(x)
  return out

