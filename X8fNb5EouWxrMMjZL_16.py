
def collatz(num):
    res =[]
    while num!=1:
        if num%2==0:
            res.append(num)
            num=num/2
        else:
            res.append(num)
            num=num*3+1
    return len(res)

