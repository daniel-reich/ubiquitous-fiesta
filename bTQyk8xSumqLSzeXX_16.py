
def has_valid_price(product):
  try:
    p = product['price']
    return type(p) in [int, float] and p >= 0
  except:
    return False

