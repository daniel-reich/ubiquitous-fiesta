
def adjacent_product(lst):
  a = []
  for x in range(len(lst)-1):
    a.append(lst[x]*lst[x+1])
  return max(a)

