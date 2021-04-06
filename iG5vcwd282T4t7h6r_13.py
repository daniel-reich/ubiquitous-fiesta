
def str_to_dict(lst):
        
    a=[]
    b=[]
    for i in lst:
        a.append(i.split("=")[0])
        b.append(i.split("=")[1])
    
    dct = {}
    
    for i in range(len(lst)):
        dct[a[i]] = b[i]
        
    return (dct)

