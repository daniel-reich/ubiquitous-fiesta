
def modulo(x, y):    
    test=x-y if abs(x-y)<abs(x) else x+y    
    if abs(test) < abs(y):        
        return test
    else: 
        return modulo(test,y)

