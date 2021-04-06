
def has_valid_price(product):
  try:
    if (type(product['price']) is float or type(product['price']) is int) and product['price'] >= 0:
      return True
    else:
      return False
  except Exception as ex:
    return False

