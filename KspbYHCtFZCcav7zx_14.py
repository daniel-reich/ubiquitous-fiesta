
def bill_split(spicy, cost):
    tl = []
    for i, x in enumerate(spicy):
        if x == 'S':
            tl.append(cost[i])
        else:
            tl.append(cost[i]*.5)
    return [sum(tl), sum(cost)-sum(tl)]

