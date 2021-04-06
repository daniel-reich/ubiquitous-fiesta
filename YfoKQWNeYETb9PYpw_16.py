
def profit(info):
  price = (info["sell_price"] * info["inventory"]) - (info["cost_price"] * info["inventory"])
  return round(price)

