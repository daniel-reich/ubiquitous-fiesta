
def pizza_points(customers, min_orders, min_price):
    names=list(customers.keys())
    prices=list(customers.values())
    winners=[names[i] for i in range(len(names)) if len([j for j in prices[i] if j>=min_price])>=min_orders]
    return sorted(winners)

