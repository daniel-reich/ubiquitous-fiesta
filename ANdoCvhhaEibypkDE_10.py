
def closing_in_sum(n):
    res =[]
    n = list(str(n))
    for i in range(len(n)//2) :
        res.append(int(n[i] + n[len(n)-i-1]))
    if len(n)%2!=0 : res.append(int(n[len(n)//2]))
    return sum(res)

