
def get_total_price(groceries):
  return round(sum(i['quantity'] * i['price'] for i in groceries),1)

