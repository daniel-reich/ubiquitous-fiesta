
def has_valid_price(product):
  if product is None:
    return False
  try:
    return product and "price" in product and product["price"] >= 0 and type(product["price"]) is not str
  except:
    return False

