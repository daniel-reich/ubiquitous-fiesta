
def get_total_price(groceries):
  total = 0
  for item in groceries:
    total += item['price'] * item['quantity']
    print(total)
  return round(total, 1)

