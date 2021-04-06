
def sum_digits(m, n):
    sum=0
    for a in range(m,n+1):
            string=str(a)
            for b in string:
                    b=str(b)
                    sum+=int(b)
    return sum

