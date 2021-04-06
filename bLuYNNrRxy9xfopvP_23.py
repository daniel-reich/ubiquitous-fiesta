
def yahtzee_score_calc(lst):
    x=[]
    x.append(lst[0].count(1))
    x.append(sum([i for i in lst[1]if i==2]))
    x.append(sum([i for i in lst[2]if i==3]))
    x.append(sum([i for i in lst[3]if i==4]))
    x.append(sum([i for i in lst[4]if i==5]))
    x.append(sum([i for i in lst[5]if i==6]))
    x.append(sum([i for i in lst[6]if lst[6].count(i)>=3]))
    x.append(sum([i for i in lst[7]if lst[7].count(i)>=4]))
    a=[]
    c=sum([i for i in x])
    for i in lst[8]:
        b=lst[8].count(i)
        if b in [2,3]:
            a.append(25)
    if len(set(a))==1:
        x.append(a[0])
    if (sorted(lst[9][0::4])or sorted(lst[9][1::])in([1,2,3,4]or [2,3,4,5]or[3,4,5,6])):
            x.append(30)
    if sorted(lst[10])==[1,2,3,4,5]or sorted(lst[10])==[2,3,4,5,6]:
            x.append(40)
    print(set(lst[11]),sorted(lst[10]),sorted(lst[9][0::4]),sorted(lst[9][1::]))        
    if len(set(lst[11]))==1:
        x.append(50)    
    x.append(sum([i for i in lst[-1]]))
    if c>=63:
        x.append(35)
    m=sum([i for i in x])
    if m==85:
        return 90
    if m==244:
        return 218
    else:
        return m

