
def split_bunches(bunches):
    
    a, b = [], []
    for i in bunches:
        a.append(i["quantity"])
        i["quantity"]=1     
    for i in range(len(bunches)):
        for j in range(a[i]):
            b.append(bunches[i])        
    return b

