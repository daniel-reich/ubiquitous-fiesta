
def pizza_points(customers, min_orders, min_price):
  return sorted([k for k, v in customers.items() if len([o for o in v if o >= min_price]) >= min_orders])

