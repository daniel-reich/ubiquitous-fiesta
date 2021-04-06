
def profit(info):
  cp = info.get('cost_price')
  sp = info.get('sell_price')
  i = info.get('inventory')
  
  total = (sp-cp)*i
  
  return round(total)

