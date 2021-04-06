
def split(number):
    if number <2: return number    
    if number%3 == 0:   return int(3**(number/3))
    elif number%3 == 1: return int((3**((number-4)/3))*4)
    else: return int((3**((number-2)/3))*2)

