
def profit_margin(cost_price, sales_price):
  x = round((((sales_price-cost_price)*100)/sales_price),1)
  print (x)
  y = str(x) + ("%")
  return y

