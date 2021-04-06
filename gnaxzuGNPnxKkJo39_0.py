
def easter_date(y):
  # I have no idea what I'm doing
    g = y%19 +1
    s = (y -1600)//100 -(y -1600)//400
    l = (((y -1400)//100)*8)//25
    p = (3 +s -l -11*g)%30
    p -= 1 if p == 29 or (p == 28 and g > 11) else 0
    d = (y +(y//4) -(y//100) +(y//400))%7 
    e = p +1 +(4 -d -p)%7 
    return 'March ' + str(e +21) if e < 11 else 'April '+ str(e -10)

