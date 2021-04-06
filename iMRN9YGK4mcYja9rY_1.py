
def accumulating_product(lst):
  temp = []
  if len(lst) == 0:
    return temp
  a = 1
  for item in lst:
    a *= item
    temp.append(a)
    
  return temp

