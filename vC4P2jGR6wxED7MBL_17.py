
def larger_than_right(lst):
    res=[]
    for i in range(len(lst)-1):
        lst1=lst[i+1:]
        lst1.sort(reverse=True)
        if lst[i]>lst1[0]:
            res.append(lst[i])
    res.append(lst[-1])    
    return(res)

