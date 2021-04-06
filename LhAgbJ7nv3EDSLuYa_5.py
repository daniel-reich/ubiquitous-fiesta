
def golomb(n):
    res = [1,2]
    num = 2
    while len(res)<n:
        while res.count(num)<res[num-1]:
            res+=[num]
        num+=1
    while len(res)>n:
        res.pop()
    return res

