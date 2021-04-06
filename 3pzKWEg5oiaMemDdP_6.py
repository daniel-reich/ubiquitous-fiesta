
def most_expensive_item(products):
  return sorted([i for i in products.items()],key=lambda x:x[1])[-1][0]

