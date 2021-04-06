
def merge_arrays(a, b):
  lst = []
  for i in range(max(len(a), len(b))):
    if len(a) > i: lst += [a[i]]
    if len(b) > i: lst += [b[i]]
  return lst

