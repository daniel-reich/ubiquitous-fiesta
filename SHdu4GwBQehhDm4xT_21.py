
def freed_prisoners(prison):
    
    ff=[]
    
    if prison[0] == 0:
        return 0
    
    if prison[0] == 1:
        ff.append(1)
​
    a=[]
    for i in prison:
        if i == 0:
            a.append(1)
        else:
            a.append(0)     
    prison = a
    if prison[1] == 1:
        ff.append(1)
    
    for k in range(1, len(prison)-1):
        a=[]
        if prison[k] == 1:
            for i in prison:
                if i == 0:
                    a.append(1)
                else:
                    a.append(0)
        else:
            a=prison
        prison = a
        if prison[k+1] == 1:
            ff.append(1) 
​
    
    return(sum(ff))

