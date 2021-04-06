
def most_expensive_item(products):
  return sorted(products, key=lambda item: products[item], reverse=True)[0]

