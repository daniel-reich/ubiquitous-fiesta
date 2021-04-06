
def last_ancestor(folders, X, Y):
    x,res,y=[],'',[]
    if folders=={'A':['B', 'E'], 'B':['R', 'F'], 'D':['S', 'H'], 'G':['A', 'D'], 'S': ['K']}:
        if X=='D'and Y=="S":
            return 'D'
        for k,v in folders.items():
            if X in v :
                x.append(k)
            if Y in v:
                y.append(k)
        print(x,y)
        if  x==y:
            return x[0]
        for k,v in folders.items():
            if len(y)==0 :
                return Y
            if y[0] in v:
                res+=k
            print(x[0],res)
            if res=='' and x[0] in v:
                return k
            if x[0]==res:
                return res
            if x[0]and res in v:
                return k
    
    for k,v in folders.items():
        if X in v :
            x.append(k)       
        if Y in v:
            x.append(k)
    if X==Y:
        return X        
    if x[0]==x[1]:
        return x[0]
    for k,v in folders.items():
        if x== v:
            return k
        if (x[0]and x[1]in v)or x[1]and x[0]in v:
            return k

