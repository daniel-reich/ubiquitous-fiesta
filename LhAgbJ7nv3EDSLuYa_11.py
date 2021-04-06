
def golomb(n):    
    g = [0] * (n + 1)  
    g[1] = 1 
    for i in range(2, n + 1):  
        g[i] = 1 + g[i - g[g[i - 1]]]  
    return g[1:]

