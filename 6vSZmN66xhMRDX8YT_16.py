
def advanced_sort(lst):
  b,c=[], []
  for i in lst:
    if i not in b:
      c.append([i]*lst.count(i))
      b.append(i)
  return c

