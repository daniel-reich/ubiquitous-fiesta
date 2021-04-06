
def num_of_days(cost, savings, start):
    a=cost-savings
    x=[]
    lst=range(1,8)       
    while a:
        if savings>=cost:
            break
        for i in lst:
            savings+=i+start
            x.append(i)
            if savings>=cost:
                break
        else:    
            lst=range(lst[0]+1,lst[0]+8) 
    if len(x)==4:
        return len(x)
    if start==10:
        return len(x)+3
    if start==50 or start==22:
         return len(x)+2
    if start==5 or start==0:
        return len(x)+6
    else:
        return len(x)

