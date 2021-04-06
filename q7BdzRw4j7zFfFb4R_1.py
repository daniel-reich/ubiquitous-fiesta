
def merge_arrays(a, b):
  l = b
  for i, x in enumerate(a):
    l.insert(2*i,x)
  return l

