
def get_total_price(groceries):
  return round(sum([dct["quantity"] * dct["price"] for dct in groceries]), 2)

