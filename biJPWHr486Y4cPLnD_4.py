
def chunkify(lst, size):
  a = len(lst) // size
  b = len(lst) % size
  x = []
  for i in range(0, len(lst)-b,size):
    x.append(lst[i:i+size])
  if b != 0:
    x.append(lst[len(lst)-b:])
  return x

