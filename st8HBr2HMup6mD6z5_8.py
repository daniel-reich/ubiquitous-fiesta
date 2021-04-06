
def profit_margin(cost_price, sales_price):
  margin = (sales_price - cost_price)/ sales_price
  return "{:.1%}".format(margin)

