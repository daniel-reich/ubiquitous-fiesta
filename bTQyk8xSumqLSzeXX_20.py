
def has_valid_price(product):
  try:
    price = product['price']
    check = isinstance(price, float) or isinstance(price, int) and price >= 0
    if check: return True
  except: return False
  return False

