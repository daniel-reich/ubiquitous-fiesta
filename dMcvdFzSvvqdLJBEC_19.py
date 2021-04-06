
def num_of_days(cost, savings, start):
    d = 1
    while 21*(d//7)*(d//7+1)-6*(d//7)*d+d*(d-1)//2 + d*start < cost-savings:
        d += 1
    return d

