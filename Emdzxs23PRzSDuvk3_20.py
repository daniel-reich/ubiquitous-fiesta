
def pizza_points(customers, min_orders, min_price):
  ret = []
  for cust in customers:
    if len([ x for x in customers[cust] if x >= min_price]) >= min_orders:
      ret.append(cust)
  return sorted(ret)

