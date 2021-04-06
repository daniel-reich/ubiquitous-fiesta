
def standard_deviation(lst):
    s=0
    a=0
    for i in range(len(lst)):
        a=a+lst[i]
    r=a/len(lst)
    for i in range(len(lst)):
        f=abs(r-lst[i])
        f=f**2
        s=s+f
    return round((s/(len(lst)))**0.5,2)

