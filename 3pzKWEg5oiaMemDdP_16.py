
def most_expensive_item(products):
  return max(products.items(), key=lambda d: d[1])[0]

