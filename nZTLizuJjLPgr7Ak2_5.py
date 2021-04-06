
def additive_inverse(lst):
  for i in range(len(lst)):
    lst[i] = -lst[i] if lst[i] > 0 else abs(lst[i])
  return lst

