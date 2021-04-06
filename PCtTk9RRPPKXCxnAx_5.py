
def modulo(x, y):
    if abs(x) < abs(y):
        return x       
    else:
        if (x<0 and y>0):
            return -(modulo (abs(x)-y, y))
        elif (x>0 and y<0):
            return (modulo (x-abs(y), y))
        else:    
            return modulo (x-y, y)

