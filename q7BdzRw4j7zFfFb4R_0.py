
def merge_arrays(a, b):
  x = []
  for i in range(max(len(a), len(b))):
    if len(a) > i:
      x.append(a[i])
      
    if len(b) > i:
      x.append(b[i])
      
  return x

