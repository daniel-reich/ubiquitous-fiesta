
def num_layers(n):
    if n == 0:
        res = 0.5
    else:
        res = 2**(n-1)
        
    return str(res/1000) +"m"

