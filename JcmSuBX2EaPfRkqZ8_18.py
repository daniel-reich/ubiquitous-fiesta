
def get_total_price(groceries):
  cost = 0
  for x in groceries:
    cost += x["quantity"]*x["price"]
  return round(cost,2)

