
def has_valid_price(product):
  return product != None and "price" in product and type(product["price"]) in (int, float) and product["price"] >= 0

