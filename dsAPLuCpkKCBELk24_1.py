
def get_products(lst):
  res = []
  
  for num in lst:
    val = 1
    for product in lst:
      if product == num:
        continue
      val = val * product
    res.append(val)   
    
  return res

