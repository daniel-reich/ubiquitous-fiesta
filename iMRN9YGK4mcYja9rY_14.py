
def product(lst):
  result = 1
  for x in lst: result *= x
  return result
  
def accumulating_product(lst):
  if not lst: return []
  return [product(lst[:x]) for x in range(1,len(lst)+1)]

