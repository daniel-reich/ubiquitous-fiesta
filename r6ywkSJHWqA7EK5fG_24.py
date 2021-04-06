
def printgrid(rows, cols):
    ctr = 1
    myans =[]
    for i in range(rows):
        temp = []
        for j in range(cols):
            temp.append(0)
        myans.append(temp)
        
    
    for x in range(cols):
        for y in range(rows):
            myans[y][x] = ctr
            ctr += 1
    return myans

