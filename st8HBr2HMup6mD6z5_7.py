
def profit_margin(cost_price, sales_price):
    taux = ((int(sales_price) - int(cost_price)) / int(sales_price))
    percentage = round((taux * 100), 1)
    percentage_str = '{}{}'.format(percentage, '%').__str__()
    return percentage_str

