
def pizza_points(customers, min_orders, min_price):
  lst = []
  for k in customers :
    orders = 0 
    for item in customers[k]:
      if item >= min_price :
        orders += 1 
    if orders >= min_orders :
      lst.append(k)
  return sorted(lst)

