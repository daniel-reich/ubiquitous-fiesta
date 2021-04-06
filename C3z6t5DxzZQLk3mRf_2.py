
def tune(lst):
    freq = [329.63,246.94,196.00,146.83,110.00,82.41]
    symb = ['+<<','+<','>+','>>+',' - ','OK']
    lst2 = []
    for i,x in enumerate(lst):
        dif = x - freq[i]
        if x != 0:
            y = round(abs(dif)/x,2)
        if x == 0:
            lst2.append(symb[-2])
        elif dif == 0:
            lst2.append(symb[-1])
        elif y < .01:
            lst2.append(symb[-1])
        elif y >= .03:
            if dif < 0:
                lst2.append(symb[3])
            else:
                lst2.append(symb[0])
        elif y < .03: 
            if dif > 0:
                lst2.append(symb[1])
            else:
                lst2.append(symb[2])
    return lst2

