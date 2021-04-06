
def row_sum(n):
    f = int(1 + (n-1)*n/2)
    return  sum([f+i for i in range(n)])

