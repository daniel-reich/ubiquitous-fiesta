
def stock_picker(lst):
    res =[]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[j]-lst[i]>0:res.append(lst[j]-lst[i])
    return max(*res) if len(res)!=0 else -1

