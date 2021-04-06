
def profit_margin(cost_price, sales_price):
  profit_margin=(sales_price-cost_price)/sales_price
  return str(round(profit_margin*100,1))+'%'

