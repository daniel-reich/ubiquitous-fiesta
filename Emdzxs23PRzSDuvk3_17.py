
def pizza_points(customers, min_orders, min_price):
  eligible_names = []
  for name in customers:
    if sum(i >= min_price for i in customers[name]) >= min_orders:
      eligible_names.append(name)
      
  return sorted(eligible_names)

