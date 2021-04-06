
def generate_rug(n):
    retLst =[]
    intialNumber = int((n-1)/2)
    
    for i in range(intialNumber):
        row = []
        for j in range(i+1):
            row.append(intialNumber-j)
        loopForIntN = n - ((i+1)*2)
        if loopForIntN > 0:
            for j in range(loopForIntN):
                row.append(intialNumber-i)
        for j in range(intialNumber-i,intialNumber+1):
            row.append(j)
        
        retLst.append(row)
        
    #copy
    restLst = retLst.copy()
    restLst.reverse()
    
    #centerRow
    row=[]
    for i in range(n):
        v = abs(i- intialNumber)
        row.append(v)
    retLst.append(row)
    retLst.extend(restLst)
        
    
    return retLst

