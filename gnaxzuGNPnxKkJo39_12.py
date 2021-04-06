
def easter_date(y):
    g = y%19 + 1
    
    s = (y-1600)//100 - (y-1600)//400
    l = (((y-1400)//100)*8)//25
    
    p1 = (3 - 11*g + s - l)%30
    if (p1 == 29) or (p1 == 28 and g > 11):
        p = p1 - 1
    else:
        p = p1
    
    d =  (y + (y//4) - (y//100) + (y//400))%7 
    d1 = (8- d)%7
    p2 = (80 + p)%7
    
    x1 = d1 - p2
    
    x = (x1 - 1)%7 + 1
    e = p + x
    if e < 11:
        e = e + 21
        month = "March"
    else:
        e = e - 10
        month = "April"
    
    result = month + " " + str(e)
    
    return result

