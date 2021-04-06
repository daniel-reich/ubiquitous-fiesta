
def rolls(lst):
    k=lst[0]
    for i in range(1,len(lst)):
​
        s=lst[i]
​
        if(lst[i-1]==1):
            s=0
        if(lst[i-1]==6):
            s=2*lst[i]
​
        k=k+s
​
    return k

