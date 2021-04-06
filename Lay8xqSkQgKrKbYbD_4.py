
def climbing_stairs(cost):
    a,b=0,0
    n=len(cost)
    for i in range(n):
        c=cost[i]+min(a,b)
        b=a
        a=c
    return min(a,b)

