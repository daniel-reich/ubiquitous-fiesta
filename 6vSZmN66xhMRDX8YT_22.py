
def advanced_sort(lst):
  a = [[i]*lst.count(i) for i in lst]
  b = []
  for i in a:
    if i not in b:
      b.append(i)
  return b

