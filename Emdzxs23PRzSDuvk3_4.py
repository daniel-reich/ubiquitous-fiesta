
def pizza_points(customers, min_orders, min_price):
  lst = []
  for i in customers.keys():
    if len([x for x in customers[i] if x >= min_price]) >= min_orders:
      lst.append(i)
  return sorted(lst)

