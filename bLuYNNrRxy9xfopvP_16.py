
def yahtzee_score_calc(lst):
    sc=0
    for i in range(1,7,1):
        sc+=i*lst[i-1].count(i)
    if sc>=63:
        sc+=35
    s=set(lst[6])
    if len(s)==3:
        for i in s:
            if lst[6].count(i)==3:
                sc+=sum(lst[6])
    s=set(lst[7])
    if len(s)==1:
        sc+=sum(lst[7])
    if len(s)==2:
        for i in s:
            if lst[7].count(i)==4:
                sc+=sum(lst[7])
    s=set(lst[8])
    if len(s)==2:
        for i in s:
            if lst[8].count(i)==3:
                sc+=25
    s=sorted(lst[9])
    if s[3]-s[0]==3 or s[4]-s[1]==3:
        sc+=30   
    s=sorted(lst[10])
    if s[4]-s[0]==4 and len(set(lst[10]))==5:
        sc+=40
    if len(set(lst[11]))==1:
        sc+=50
    sc+=sum(lst[12])
    return sc

