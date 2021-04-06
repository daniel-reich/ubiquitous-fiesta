
def sle(m):
    la = m[0]
    lb = m[1]
​
    val = 0
    for val in range(1, 100):
        if((val / la[0]) == (val // la[0]) and
           (val / lb[0]) == (val // lb[0])):
            break
​
    laP = la[:]
    m = val / laP[0]
    laP[0] *= m
    laP[1] *= m
    laP[2] *= m
    
    lbP = lb[:]
    m = val / lbP[0]
    lbP[0] *= m
    lbP[1] *= m
    lbP[2] *= m
​
    if(abs(laP[1]) == abs(lbP[1])):
        return False
        
​
    #print(laP, " ", lbP)
​
    cy = laP[1] - lbP[1]
    c = laP[2] - lbP[2]
    y = c / cy
​
    x = (la[2] - (la[1] * y)) / la[0]
​
    #print(x, " ", y)
​
    return (x, y)

