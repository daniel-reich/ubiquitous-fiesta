
def majority_vote(lst):
    b=0
    for i in range(0,len(lst)):
        a=0
        for j in range(0,len(lst)):
             if lst[i]==lst[j]:
                 a=a+1
        if a>b:
            b=a
            index=i
    if b>len(lst)/2:
        return lst[index]
    else:
        return None

