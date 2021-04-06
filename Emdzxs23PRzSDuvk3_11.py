
def pizza_points(customers, min_orders, min_price):
  return sorted([x for x in customers if len([i for i in customers[x] if i >= min_price]) >= min_orders])

