
def simplify_sqrt(n):
    for i in range(1, n):
        if  n % i == 0:
            a = (n // i) ** 0.5
            if a == int(a):
                return (int(a), i)
    return(1, n)

