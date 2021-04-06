
def profit(info):
  revenue = info['inventory'] * info['sell_price']
  unit_cost = info['cost_price'] * info['inventory']
  return round(revenue - unit_cost)

