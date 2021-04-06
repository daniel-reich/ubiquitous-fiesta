
def most_expensive_item(products):
  m = max(products.values())
  for i in products:
    if products[i] == m:
      return i

