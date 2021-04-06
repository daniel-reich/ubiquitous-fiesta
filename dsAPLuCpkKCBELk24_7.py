
def get_products(lst):
  res = []
  prod = 1
  for idx in range(len(lst)): 
    for item in lst:
      if item != lst[idx]:
        prod *= item
    res.append(prod)
    prod = 1
  return res

