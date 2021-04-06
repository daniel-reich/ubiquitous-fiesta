
def get_total_price(groceries):
  total = sum(x.get('quantity') * x.get('price') for x in groceries)
  return round(total, 1)

