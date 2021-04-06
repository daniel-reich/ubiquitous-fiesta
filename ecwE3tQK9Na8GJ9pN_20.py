
def little_big(n):
    x = 100
    if n == 2:
        return x
    elif n % 2 == 0:
        n = n//2
        for i in range(0,n-1):
            x = x*2
        return x
    elif n % 2 != 0 :
        y  = (n-1)/2 +5
        return y
little_big(10)

