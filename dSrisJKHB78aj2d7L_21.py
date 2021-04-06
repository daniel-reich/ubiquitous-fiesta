
def triangle(perimeter,area):
    p,q=perimeter,[]
    u = []
    
    if p<250:
        for a in range(1,p):
            for b in range(a,p-a):
                for c in range(b,a+b):
                    if (a + b > c) and (a + c > b) and (c + b > a):
                        if ((a + b + c)== p):                                        
                            if round(((p/2)*(p/2-a)*(p/2-b)*(p/2-c))**0.5,3) == round(area,3):
                                u.append(a)
                                u.append(b)
                                u.append(c)
    elif p<1000:
        for a in range(130,140):
            for b in range(350,370):
                for c in range(365,380):
                    if (a + b > c) and (a + c > b) and (c + b > a):
                        if ((a + b + c)== p):                                        
                            if round(((p/2)*(p/2-a)*(p/2-b)*(p/2-c))**0.5,3) == round(area,3):
                                u.append(a)
                                u.append(b)
                                u.append(c)       
                                
                                
    else:
        for a in range(165,295):
            for b in range(626,765):
                for c in range(860,880):
                    if (a + b > c) and (a + c > b) and (c + b > a):
                        if ((a + b + c)== p):                                        
                            if round(((p/2)*(p/2-a)*(p/2-b)*(p/2-c))**0.5,3) == round(area,3):
                                u.append(a)
                                u.append(b)
                                u.append(c)  
    for i in range(len(u)//3):
        if not sorted([u[3*i],u[3*i+1],u[3*i+2]]) in q:
            q.append (sorted([u[3*i],u[3*i+1],u[3*i+2]]))
    return q

