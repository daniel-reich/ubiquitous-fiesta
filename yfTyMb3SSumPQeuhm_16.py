
def fibonacci(n):
    return doubling(n)[0]
​
def doubling(n):
    if n == 0:
        return(0,1)
    else:
        x,y = doubling(n//2)
        k = x*(y*2 - x)
        k1 = x**2 + y**2
        if n%2 == 0:
            return(k,k1)
        else:
            return(k1, k+k1)

