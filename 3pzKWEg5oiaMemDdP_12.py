
def most_expensive_item(products):
  return max(products.items(), key=lambda p: p[1])[0]

