
def simplify(str_fraction):
    largest_devisor = 1
    fraction = str_fraction.split('/')
    for f in range(len(fraction)): fraction[f] = int(fraction[f])
    for devisor in range(1,fraction[0]+1):
        test = fraction[0]/devisor
        if(test == int(test)):  
            test = fraction[1]/devisor
            if(test == int(test)):  largest_devisor = devisor
    
    simp_fraction = []
    simp_fraction.append(int(fraction[0]/largest_devisor))
    simp_fraction.append(int(fraction[1]/largest_devisor))
​
    out_fraction = ""
    if(simp_fraction[1] == 1):
        out_fraction = out_fraction + str(simp_fraction[0])
    else:
        out_fraction = out_fraction + str(simp_fraction[0]) + "/" + str(simp_fraction[1])
    return(out_fraction)

