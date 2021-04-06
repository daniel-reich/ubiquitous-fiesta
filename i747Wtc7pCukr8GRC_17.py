
def max_product(lst):
    import itertools
    comblst=[]
    for comb in itertools.combinations(lst, 3):
        comblst.append(comb)
    #print(comblst)
    anslst = sorted([i[0]*i[1]*i[2] for i in comblst])
    return anslst[-1] 
​
def min_product(lst):
    import itertools
    comblst=[]
    for comb in itertools.combinations(lst, 3):
        comblst.append(comb)
    #print(comblst)
    anslst = sorted([i[0]*i[1]*i[2] for i in comblst])
    return anslst[0]

