
def pizza_points(customers, min_orders, min_price):
    rewarded_customers = []
    for customer, orders in customers.items():
        checked_prizes = [1 for cost in orders if cost >= min_price]
        if len(checked_prizes) >= min_orders:
            rewarded_customers.append(customer)
    return sorted(rewarded_customers)

