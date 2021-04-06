
def eda_bit(start, end):
    a=[]
    for x in range(start,end+1):
        if x%3==0 and x%5==0 or x==0:
            a.append("EdaBit")
        elif x%3==0:
            a.append("Eda")
        elif x%5==0:
            a.append("Bit")
        else:
            a.append(x)
    return a

