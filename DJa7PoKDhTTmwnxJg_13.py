
def adjacent_product(lst):
  x = []
  for i in range(len(lst) - 1):
    x.append(lst[i] * lst[i + 1])
  return max(x)

