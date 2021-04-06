
def most_expensive_item(products):
  ma = max(products.values())
  for key, values in products.items():
    if values == ma:
      return key

