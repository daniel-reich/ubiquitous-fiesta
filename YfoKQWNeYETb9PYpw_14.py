
def profit(info):
  cost_price=info.get("cost_price")
  sales_price=info.get("sell_price")
  total_profit=(sales_price-cost_price)*info.get("inventory")
  return round(total_profit)

