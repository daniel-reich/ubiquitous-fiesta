
def adjacent_product(lst):
  products = []
  for i in range(0,len(lst)-1):
    products.append(lst[i]*lst[i+1])
  return max(products)

