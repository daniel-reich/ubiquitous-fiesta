
def fibo(n):
    a = 1
    b = 1
    if n == 0: 
        return 0 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b

