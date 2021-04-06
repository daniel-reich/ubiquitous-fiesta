
def get_products(lst):
  prod_list = []
  
  for i in lst:
    product = 1
    mylst = [x for x in lst if x != i]
    for j in mylst:
      product *= j
    prod_list.append(product)
    
  return prod_list

