
def profit(info):
  p = info['sell_price'] - info['cost_price']
  total_profit = p*info['inventory']
  return round(total_profit)

