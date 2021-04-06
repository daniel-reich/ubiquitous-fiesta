
def pizza_points(customers, min_orders, min_price):
  lst = []
  for x, i in customers.items():
    if len([a for a in i if a >= min_price]) >= min_orders:
      lst.append(x)
  return sorted(lst)

