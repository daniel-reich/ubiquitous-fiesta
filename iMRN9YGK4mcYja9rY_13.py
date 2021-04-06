
def accumulating_product(lst):
  if len(lst) == 0:
    return []
    
  accum = lst[0]
  result = [accum]
  for i in range(1, len(lst)):
    accum *= lst[i]
    result.append(accum)
    
  return result

