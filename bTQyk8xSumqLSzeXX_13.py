
def has_valid_price(product):
  try:
    return product['price'] >= 0
  except:
    return False

