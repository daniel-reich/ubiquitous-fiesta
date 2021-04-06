
def most_expensive_item(products):
  products = sorted(products.items(), key = lambda kv: kv[1], reverse = True)
  return products[0][0]

