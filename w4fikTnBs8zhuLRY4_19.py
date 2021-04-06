
def rep_set(n):
  arr = []
  for i in range(0,n):
    t = []
    for x in arr:
      t.append(x)
    arr.append(t)
  return arr

