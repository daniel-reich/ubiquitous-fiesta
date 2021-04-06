
def countdown(operands, target):
    op=list(operands)
    v, w, x, y= [], [], [], ["+", "-", "*", "//"]
    t=["1"]
    if len(op)==2:
        for a in op:
            for b in op:
                x.append([str(a),str(b)])
        for i in x:
            for j in i:
                if i.count(j)>1:
                    v.append(i)
        for i in v:
            if i in x:
                x.remove(i)
        for i in range(len(x)):
            x[i]=[x[i][0]]+t+[x[i][1]]       
            for p in y:
                    x[i][1]=p
                    if eval("".join(x[i]))==target:
                        return("".join(x[i]))  
​
    if len(op)==3:
        for a in op:
            for b in op:
                for c in op:
                    x.append([str(a),str(b),str(c)])
        for i in x:
            for j in i:
                if i.count(j)>1:
                    v.append(i)
        for i in v:
            if i in x:
                x.remove(i)
        for i in range(len(x)):
            x[i]=[x[i][0]]+t+[x[i][1]]+t+[x[i][2]]        
            for p in y:
                    for q in y:
                        x[i][1],x[i][3]=p,q
                        if eval("".join(x[i]))==target:
                            return("".join(x[i])) 
    if len(op)==4:
        for a in op:
            for b in op:
                for c in op:
                    for d in op:
                        x.append([str(a),str(b),str(c),str(d)])
        for i in x:
            for j in i:
                if i.count(j)>1:
                    v.append(i)
        for i in v:
            if i in x:
                x.remove(i)
        for i in range(len(x)):
            x[i]=[x[i][0]]+t+[x[i][1]]+t+[x[i][2]]+t+[x[i][3]]      
            for p in y:
                    for q in y:
                        for r in y:
                            x[i][1],x[i][3],x[i][5] =p,q,r
                            if eval("".join(x[i]))==target:
                                return("".join(x[i]))                          
                        
    if len(op)==5:
        for a in op:
            for b in op:
                for c in op:
                    for d in op:
                        for e in op:
                            x.append([str(a),str(b),str(c),str(d),str(e)])
        for i in x:
            for j in i:
                if i.count(j)>1:
                    v.append(i)
        for i in v:
            if i in x:
                x.remove(i)
        for i in range(len(x)):
            x[i]=[x[i][0]]+t+[x[i][1]]+t+[x[i][2]]+t+[x[i][3]]+t+[x[i][4]]        
            for p in y:
                    for q in y:
                        for r in y:
                            for s in y:
                                x[i][1],x[i][3],x[i][5],x[i][7] =p,q,r,s
                                if eval("".join(x[i]))==target:
                                    return("".join(x[i]))

