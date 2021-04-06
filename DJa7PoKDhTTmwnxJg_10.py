
def adjacent_product(lst):
  m = lst[0] * lst[1]
  for i in range(len(lst) - 1): 
    if lst[i] * lst[i + 1] > m:
      m = lst[i] * lst[i + 1]
  return m

