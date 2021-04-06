
def lcm(n):
    x=n[0]
    for i in n[1:]:
        if x > i: 
            s = i 
        else: 
            s = x 
        for y in range(1, s+1): 
            if((x % y == 0) and (i % y == 0)): 
                gcd = y
        x = x*i//gcd   
    return x

