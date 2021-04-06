
def sum_of_two(a, b, v):
  L = []
  for i in a:
    for u in b:
      L.append(i+u)
  if v in L:
    return True
  return False

