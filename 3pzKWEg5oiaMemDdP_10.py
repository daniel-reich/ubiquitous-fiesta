
def most_expensive_item(products):
  return [i for i, j in products.items() if products[i] == max(j for j in products.values())][0]

