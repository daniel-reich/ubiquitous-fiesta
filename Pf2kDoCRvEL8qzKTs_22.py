
def order_people(lst, people):
    if lst[0]*lst[1]<people:
        return "overcrowded"
    llst=[ [] for r in range(lst[0])]
    cnt=0
    for i in range (1,lst[0]*lst[1],lst[1]): 
        for m in range(i,i+lst[1]):
            if m>people:
                 llst[cnt].append(0)
            else:
                llst[cnt].append(m)
        cnt+=1
    return list(map(lambda x : x[::-1] if llst.index(x)%2==1 else x, llst ))

