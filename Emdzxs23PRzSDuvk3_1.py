
def pizza_points(customers, min_orders, min_price):
  return sorted([customer for customer,orders in customers.items() if len([price for price in orders if price >= min_price]) >= min_orders])

