
def smallest(n):
    if n == 1:
        return 1
    else:
        m=smallest(n-1)
        if m%n==0:
            return m
        else:
            off=m%n
            for i in range(m,(n*m)+1, m):
                if (i%n == 0) and (i%m == 0):
                    return i

