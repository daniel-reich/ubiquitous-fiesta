
def adjacent_product(lst):
  product = lst[0]*lst[1]
  for i in range(len(lst)-1):
    if lst[i]*lst[i+1] >= product:
      product = lst[i]*lst[i+1]
  return product

