
def pizza_points(customers, min_orders, min_price):
    lst = []
    for key in customers.keys():
        if sum(j >= min_price for j in customers[key]) >= min_orders:
            lst.append(key)
            
    return sorted(lst)

