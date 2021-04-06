
def max_product(lst):
    n_l=[x for x in lst if x < 0]
    l=len(n_l)
    lst1=sorted(lst)
    prd=lst1[-1]*lst1[-2]*lst1[-3]
    if l>=2 and prd >=0:
        if lst1[0]*lst1[1] > lst1[-1]*lst1[-2]:
            prd=lst1[0]*lst1[1]*lst1[-1]
    return prd        
def min_product(lst):
    n_l=[x for x in lst if x < 0]
    l=len(n_l)
    lst1=sorted(lst)
    prd=lst1[0]*lst1[1]*lst1[2]
    if l>=1:
        if lst1[0]*lst1[1]*lst1[2] > lst1[0]*lst1[-2]*lst1[-1]:
            prd=lst1[0]*lst1[-2]*lst1[-1]
    return prd

