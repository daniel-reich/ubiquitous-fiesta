
def safecracker(start, i):
    if start-i[0] > 0:        
        one=start-i[0]
    else:
        one=100-abs(i[0]-start)
    ###########    
    if one+i[1]<100:        
        two=one+i[1]
    else:
        two=abs(100-(one+i[1]))
    ###########
    if two-i[2] > 0:        
        tre=two-i[2]
    else:
        tre=100-abs(two-i[2])
    return [one,two,tre]

