
def clear_ordering(lst):
  order1 = [ls[0] for ls in lst]
  order2 = [ls[1] for ls in lst]
  
  for order in order2:
    if order2.count(order) > 1:
      return False
      break
  for order in order1:
    if order1.count(order) > 1:
      return False
      break
  return True

