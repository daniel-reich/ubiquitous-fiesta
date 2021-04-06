
def safecracker(start, increments):
    combination = []
​
    count=0
​
    if start == 0:
        start = 100
    comb1 = start
    
    while increments[0] != count and start != 0 and comb1 !=0:
        comb1 = comb1-1 
        count=count+1
      
        if comb1 == 0:
            comb1 = 100
        if count == increments[0]:
       
            combination.append(comb1)
​
    
​
    count2=0
    if comb1 == 100:
        comb1 = 0
    comb2=comb1
    
    while increments[1] != count2 and comb2 != 100:
        comb2 = comb2 + 1
        count2 = count2+1
       
        if comb2 == 100:
            comb2 = 0
        if count2 == increments[1]:
            combination.append(comb2)
​
    count3=0
    if comb2 == 0:
        comb2 = 100
    comb3=comb2
    while increments[2] != count3 and comb3 != 0:
        comb3 = comb3-1
        count3 = count3+1
        if comb3 == 0:
            comb3 = 100
        if count3 == increments[2]:
            combination.append(comb3)
​
​
​
    return(combination)

