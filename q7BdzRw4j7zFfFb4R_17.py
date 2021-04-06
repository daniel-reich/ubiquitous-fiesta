
def merge_arrays(a, b):
  [a.insert((i*2)+1,b[i]) for i in range(len(b))]
  return a

