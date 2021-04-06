
def has_valid_price(product):
  def valid_price(price):
    return (isinstance(price, int) or isinstance(price, float)) and price >= 0.
​
  return product is not None and "product" in product and "price" in product and valid_price(product["price"])

