
def get_total_price(groceries):
  return round(sum(g["quantity"]*g["price"] for g in groceries),1);

