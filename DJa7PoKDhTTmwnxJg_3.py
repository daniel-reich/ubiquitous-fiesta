
def adjacent_product(lst):
  return max(a * b for a, b in zip(lst, lst[1:]))

