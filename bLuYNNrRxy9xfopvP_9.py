
def yahtzee_score_calc(lst):
    res=0
    for i in range(1,7):
        res+=(lst[i-1].count(i))*i
    if res>=63:
        res+=35
    store=dict()
    for j in range(6,12):
        freq=[0,0,0,0,0,0]
        for i in range(5):
            freq[lst[j][i]-1]+=1
        store[j]=freq 
    res+=sum(lst[6]) if any([1 if store[6][i]>=3 else 0 for i in range(6)]) else 0
    res+=sum(lst[7]) if any([1 if store[7][i]>=4 else 0 for i in range(6)]) else 0
    res+=25 if 3 in store[8] and 2 in store[8] else 0
    res+=30 if all([1 if store[9][i]==1 else 0 for i in range(4)]) or all([1 if store[9][i]==1 else 0 for i in range(1,5)]) or all([1 if store[9][i]==1 else 0 for i in range(2,6)]) else 0
    res+=40 if all([1 if store[10][i]==1 else 0 for i in range(5)]) or all([1 if store[10][i]==1 else 0 for i in range(1,6)]) else 0
    res+=50 if any([1 if store[11].count(i)==5 else 0 for i in range(6)]) else 0
    res+=sum(lst[12])
    return res

