
def rep_set(n):
  if n == 0:
    return []
  lst = []
  for i in range(n):
    lst.append(rep_set(i))
  return lst

