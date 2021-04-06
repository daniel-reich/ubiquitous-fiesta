
def merge_arrays(a, b):
  i=1
  for e in b:
    a.insert(i, e)
    i+=2
  return a

