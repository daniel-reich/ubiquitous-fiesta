
def three_sum(lst):
​
    from itertools import combinations
​
    if len(lst) < 3: 
        return []
    o=[]
​
    for i in range(1, len(lst)+1):
        for case in combinations(lst, i):
            if sum(list(case))==0 and len(list(case))==3 and list(case) not in o :
                o.append(list(case))
    return o

