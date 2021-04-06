
def profit(info):
    profit = (info["sell_price"]-info["cost_price"])*info["inventory"]
    return round(profit)

