
def profit_margin(cost_price, sales_price):
  profit = ((sales_price-cost_price) / sales_price) * 100
  return "{}%".format(round(profit, 1))

