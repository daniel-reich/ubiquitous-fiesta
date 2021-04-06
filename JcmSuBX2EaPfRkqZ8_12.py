
def get_total_price(groceries):
  total = 0
  for eachfood in groceries:
    x = eachfood['quantity']
    y = eachfood['price'] * x
    total += y
  return round(total,1)

