
def chemical_reactions(carbon, hydrogen, oxygen):
    myans = []
    
    ctr = 0
    while hydrogen > 1 and oxygen > 0:
        ctr += 1
        hydrogen -= 2
        oxygen -= 1
    myans.append(ctr)
    
    ctr = 0
    while oxygen > 1 and carbon > 0:
        ctr += 1
        oxygen -= 2
        carbon -= 1
    myans.append(ctr)
    
    ctr = 0
    while hydrogen > 1 and carbon > 0:
        ctr += 1
        hydrogen -= 4
        carbon -= 1
    myans.append(ctr)   
    
    return myans

