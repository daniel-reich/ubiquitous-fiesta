
def split(n):
    max = 1    
    for i in range (2,n):        
        if  (n/i)**i  > max:
            max = (n/i)**i
    return int ((max * 10 + .5))/10

