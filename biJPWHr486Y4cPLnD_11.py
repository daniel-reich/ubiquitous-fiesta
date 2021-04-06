
def chunkify(lst, size):
  a = lst
  chunk = size
  b = []
  for i in range(0,len(a), chunk):
    if (i+chunk) > len(a):
      b.append(a[i:])
      break
    b.append(a[i:i+chunk])
  return b

