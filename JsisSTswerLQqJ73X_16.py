
def priority_sort(l, s):
  a=sorted([i for i in l if i in s])
  b=sorted([i for i in l if i not in s])
  return a+b

