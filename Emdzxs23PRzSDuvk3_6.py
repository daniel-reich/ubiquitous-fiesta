
def pizza_points(customers, min_orders, min_price):
  l=[]
  for x in customers:
    if len([i for i in customers[x] if i>=min_price])>=min_orders: l.append(x)
  return sorted(l)

