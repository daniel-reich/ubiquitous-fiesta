
def lottery(ticket,win):
    z=0
    for i in ticket :
        y =[]
        for y in [i]:       
            if chr(y[1]) in y[0]:\
                z=z+1    
            
    if z>= int(win):
        a="Winner!"
    else:
        a="Loser!"               
    return a

