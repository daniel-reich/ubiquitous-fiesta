
def pentagonal(n):
    if n ==1:
        return 1
    else:
        return 5*(n-1) + pentagonal(n-1)

