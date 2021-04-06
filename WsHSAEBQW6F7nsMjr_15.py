
def flatten_the_curve(lst):
    if len(lst)==0:
        return lst
    sum=0
    for i in lst:
        sum=sum+i
    mean=sum/len(lst)
    mean=round(mean,1)
    le=len(lst)
    lst.clear()
    for i in range(le):
        lst.append(mean)
    return lst

