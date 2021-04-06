
def pizza_points(customers, min_orders, min_price):
  eligible = []
  for customer, orders in customers.items():
    i = 0
    for order in orders:
      if order >= min_price: i += 1
    if i >= min_orders: eligible.append(customer)
  
  return sorted(eligible)

