
def adjacent_product(lst):
  return max(i*j for i, j in zip(lst, lst[1:]))

