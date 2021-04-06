
def profit_margin(cost_price, sales_price):
    profit_m = (sales_price-cost_price)/sales_price*100
    return "{:.1f}%".format(profit_m)

