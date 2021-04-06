
def power_ranger(power, minimum, maximum):
    i=int(minimum**(1/power))
    j=0
    if i**power==minimum:
       j=1
    while i**power<=maximum:
        j+=1
        i+=1
    return(j-1)

