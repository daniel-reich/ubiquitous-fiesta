
def has_valid_price(product):
  if product is None:
    return False
  return product and "price" in product and product["price"] is not None and isinstance(product["price"], (float, int)) and product["price"] >= 0

