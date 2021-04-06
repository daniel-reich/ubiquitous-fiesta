
def sexagenary(year):
    b = ['Rat','Ox','Tiger','Rabbit','Dragon','Snake','Horse','Sheep','Monkey','Rooster','Dog','Pig']
    s = ['Wood','Wood','Fire','Fire','Earth','Earth','Metal','Metal','Water','Water']
    x = 1984
    
    y = year - 1984
    
    bb = b[y%12]
    ss = s[y%10]
    
    return ss+' '+bb

