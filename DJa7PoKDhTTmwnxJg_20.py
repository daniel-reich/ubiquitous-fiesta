
def adjacent_product(lst):
  return max(lst[i]*num for i, num in enumerate(lst[1:]))

