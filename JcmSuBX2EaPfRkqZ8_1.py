
def get_total_price(groceries):
    cost = 0
    for product in groceries:
        cost += product['quantity'] * product['price']
    return round(cost, 2)

