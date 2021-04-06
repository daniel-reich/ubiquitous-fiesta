
def rep_set(n):
  lst = []
  for i in range(n):
    if i == 0:
      s = []
      lst.append(s)
    else:
      lst.insert(i,lst[:])
  return lst

