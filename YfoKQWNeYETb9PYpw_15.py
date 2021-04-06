
def profit(info):
  exp = info['cost_price'] * info['inventory']
  rev = info['sell_price'] * info['inventory']
  return round(rev - exp)

