
def cutting_grass(lst, *cuts):
    cuts=list(cuts)
    w,x,y,z=[],[],[],[]
    a,b,c=cuts[0],cuts[1],cuts[2]
    if 1  in lst or 0  in lst:
        for i in lst:
            if i-a==0 or i-a==1:
                w.append("Done")
        return w
    elif 1 not in lst or 0 not in lst:
        for i in lst:
            if i-a==1or i-a==0:
                x.append('Done')
            else:
                x.append(i-a)
    if 'Done' in x:
        return ['Done','Done','Done']
    if 1 not in x or 0 not in x:        
        for i in x:  
            y.append(i-b)        
        for i in y:
            z.append(i-c)
    if y.count(1)==2:
        return [x,y,"Done"]
    if len(set(z))==1 or z.count(1)>2:
        return [x,y,z,'Done']
    else:
        return [x,y,z]

