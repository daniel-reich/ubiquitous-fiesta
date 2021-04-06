
def count_digits(n, d):
    lst = str([i**2 for i in range(0,n+1)])
    return lst.count(str(d))

