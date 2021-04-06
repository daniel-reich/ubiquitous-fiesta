
def has_valid_price(product):
  if not product: return False
  try:
    return type(product['price']) in (int, float) and product['price'] >= 0
  except KeyError:
    return False

