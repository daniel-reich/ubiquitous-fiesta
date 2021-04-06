
def climbing_stairs(cost):
    n = len(cost)
    price = [0] * n
    for i in range(2, n):
        price[i] = min(price[i-2] + cost[i-2], price[i-1] + cost[i-1])
    return min(price[-2] + cost[-2], price[-1] + cost[-1])

