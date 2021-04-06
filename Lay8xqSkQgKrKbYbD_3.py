
def climbing_stairs(cost):
    for i in range(0, len(cost) - 2):
        cost[i + 2] += min(cost[i], cost[i + 1])
    return min(cost[-2], cost[-1])

