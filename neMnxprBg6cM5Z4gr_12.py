
def arithmetic_progression(start, diff, n):
    #return [i for i in range(start,n+1,abs(diff))]
    #return 1 if n==1 else start+(n-1)*diff
    return ', '.join([str(start+(diff*i)) for i in range(n)])

