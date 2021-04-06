
def salt(t):
    saltAmount = 10.0 #kg
    
    
    index = 1
    while index <= t*60*1000:
        saltAmount = saltAmount + 0.100/60.000/1000 - saltAmount/10.0/60.000/1000
        index+=1
    
    return round(saltAmount, 3)

