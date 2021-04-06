
def get_total_price(groceries):
  return round(sum(x['quantity'] * x['price'] for x in groceries),1)

