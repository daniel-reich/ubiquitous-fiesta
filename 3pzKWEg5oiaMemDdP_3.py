
def most_expensive_item(products):
  return max(products.keys(), key= lambda p: products[p])

