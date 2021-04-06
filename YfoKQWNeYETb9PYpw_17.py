
def profit(info):
  profit = (info["sell_price"] - info["cost_price"]) * info["inventory"]
  return int(format(profit, ".0f"))

