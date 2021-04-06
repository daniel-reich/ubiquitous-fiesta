
def has_valid_price(product):
  if product == None or not ("price" in product):
    return False
  elif not (isinstance(product["price"],int) or isinstance(product["price"],float)):
    return False
  elif product["price"] < 0:
    return False
  else:
    return True

