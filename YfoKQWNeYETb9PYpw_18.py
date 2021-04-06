
def profit(info):
  p=info.get('inventory')*(info.get('sell_price')-info.get('cost_price'))
  return round(p)

