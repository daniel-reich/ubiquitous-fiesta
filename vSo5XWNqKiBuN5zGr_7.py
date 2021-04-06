
def divide(x, y, divisor = 0):
    if abs(x) < abs(y):
        return divisor       
    else:
        if (x<0 and y>0):
            return -(divide (abs(x)-y, y, divisor+1))
        elif (x>0 and y<0):
            return -(divide (x-abs(y), y, divisor + 1))
        else:    
            return divide (x-y, y, divisor+1)

