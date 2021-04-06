
def pizza_points(customers, min_orders, min_price):
    s = list(map(lambda x:list(x),list(customers.items())))
    s = list(map(lambda x:[x[0], list(filter(lambda x:x>=min_price,x[1]))], s))
    ans = list(filter(lambda x:len(x[1]) >= min_orders,s))
    return sorted(list(map(lambda x:x[0], ans)))

