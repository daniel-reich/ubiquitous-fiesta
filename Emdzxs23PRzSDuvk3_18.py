
def pizza_points(customers, min_orders, min_price):
  return sorted([key for key in customers if sum(pizza >= min_price for pizza in customers[key]) >= min_orders])

