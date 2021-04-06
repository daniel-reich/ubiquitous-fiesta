
def has_valid_price(product):
  if product:
    if "price" in product:
      if isinstance(product["price"],int) and product["price"]>=0:
        return True
      elif isinstance(product["price"],float) and product["price"]>=0:
        return True
  return False

