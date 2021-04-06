
def pizza_points(customers, min_orders, min_price):
  ret = []
  for customer in customers:
    orders = customers[customer]
    count = 0
    for order in orders:
      if order >= min_price:
        count += 1
    if count >= min_orders:
      ret.append(customer)
  return sorted(ret)

