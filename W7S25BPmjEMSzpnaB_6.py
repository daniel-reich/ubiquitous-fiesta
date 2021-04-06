
def bonacci(n,k):
    res = [0]*(n-1)+[1]
    for i in range(n,k+1):
        res+=[sum([x for x in res[i-n:i]])]
    return res[k-1]

