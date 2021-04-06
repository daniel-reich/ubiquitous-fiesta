
def get_total_price(groceries):
  return round(sum([d['quantity'] * d['price'] for d in groceries]),1)

