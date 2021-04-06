
def divisible_by_left(n):
    res =[False]
    n = list(map(lambda x:int(x),list(str(n))))
    for i in range(1,len(n)):
        if (n[i-1]==0):res.append(False)
        else :res.append(n[i] % n[i-1] ==0 )
    return res

