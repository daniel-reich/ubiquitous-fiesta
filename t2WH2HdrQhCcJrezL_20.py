
def eda_bit(start, end):
    res=[]
    for i in range(start, end+1):
        if i%3==0 and i%5==0:
            res.append("EdaBit")
        elif i%3==0:
            res.append("Eda")
        elif i%5==0:
            res.append("Bit")
        else:
            res.append(i)
    return res

