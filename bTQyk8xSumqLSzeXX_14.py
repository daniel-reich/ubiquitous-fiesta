
def has_valid_price(product):
  try:
    price = product['price']
    return price >= 0 and len(str(price)) == 1 or len(str(price)) == 3
  except:
    return False

