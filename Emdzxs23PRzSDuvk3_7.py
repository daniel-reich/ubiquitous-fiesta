
def pizza_points(customers, min_orders, min_price):
  out = []
  for i in customers:
    x = 0
    for j in customers[i]:
      if j >= min_price: x += 1
    if x >= min_orders:
      out.append(i)
  return sorted(out)

