
def get_products(lst):
  new = []
  for x in range(len(lst)):
    product = 1
    for y in range(len(lst)):
      if y != x:
        product *= lst[y]
    new.append(product)
  return new

