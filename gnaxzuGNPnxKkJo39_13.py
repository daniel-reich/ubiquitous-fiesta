
def easter_date(y):
    g = (y % 19) + 1
    
    s = (y - 1600) // 100 - (y - 1600) // 400
    l = (((y - 1400) // 100) * 8) // 25   
    
    pas = (3 - 11 * g + s - l) % 30
    if (pas == 29) or (pas == 28 and g > 11):
       p = pas - 1
    else:
       p = pas
       
    d = (y + (y // 4) - (y // 100) + (y // 400)) % 7
    dom = (8 - d) % 7
​
    pas_day = (80 + p) % 7
    
    x_dif = dom - pas_day
    x = ((x_dif-1)%7) + 1
    
    e = p + x
    
    if e < 11:
        return 'March ' + str(e+21)
    else:
        return 'April ' + str(e-10)

