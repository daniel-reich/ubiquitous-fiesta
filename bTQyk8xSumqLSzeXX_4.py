
def has_valid_price(product):
  if type(product) is dict and 'price' in product.keys():
    return (product['price'] >= 0) if type(product['price']) in (int, float) else False
  return False

