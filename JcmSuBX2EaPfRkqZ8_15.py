
def get_total_price(groceries):
  return round(sum(product['quantity'] * product['price'] for product in groceries), 1)

