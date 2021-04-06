
def adjacent_product(lst):
  max = -float('inf')
  for i in range(len(lst) - 1):
    if max < lst[i] * lst[i + 1]:
      max = lst[i] * lst[i + 1]
  return max

