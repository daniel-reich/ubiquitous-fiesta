
def darts_solver(sections, darts, target):        
    p,q=[],[]
    if darts == 3:
        for a in sections:
            for b in sections:
                for c in sections:
                    if (a + b + c)== target:
                        z=[]
                        z.append(a)
                        z.append(b)
                        z.append(c)
                        if len(z)>1:            
                            if not (sorted(z) in p): p.append(sorted(z))
    elif darts == 4:
        for a in sections:
            for b in sections:
                for c in sections:
                    for d in sections:
                        if (a + b + c + d)== target:
                            z=[]
                            z.append(a)
                            z.append(b)
                            z.append(c)
                            z.append(d)
                            if len(z)>1:            
                                if not (sorted(z) in p):p.append(sorted(z)) 
    for i in p: 
        for j in range(len(i)): i[j]=str(i[j])
        q.append("-".join(i))
    return q

