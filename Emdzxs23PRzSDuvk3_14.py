
def pizza_points(customers, min_orders, min_price):
  l = []
  for i, v in customers.items():
    count = 0
    for x in v:
      if x >= min_price:
        count += 1
    if count >= min_orders:
      l.append(i)
  return sorted(l)

