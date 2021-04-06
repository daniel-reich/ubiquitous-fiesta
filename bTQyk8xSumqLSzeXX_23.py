
def has_valid_price(product):
  return False if not product else product and False if "price" not in product.keys() else \
    (isinstance(product["price"], int) or isinstance(product["price"], float)) and product["price"] >= 0

