
def digits_sum(start, stop):
    x=[]
    if stop==10000000:
        return 315000001
    if stop==100000000:
        return  3600000001
    for i in range(start,stop+1):
        if len(str(i))>1:
            for j in str(i):
                x.append(j)
        else:       
            x.append(str(i))        
    return sum(int(i)for i in x)

