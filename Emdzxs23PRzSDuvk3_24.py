
def pizza_points(customers, min_orders, min_price): 
    holder = []
​
    for customer, order_price in customers.items():
        orders = 0
        for price in order_price:
            if price >= min_price:
                orders += 1
        if orders >= min_orders:
            holder.append(customer)               
​
    return sorted(holder)

