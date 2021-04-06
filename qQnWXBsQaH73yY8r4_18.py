
def fact(x):
    n = 1
    for i in range(2, x+1):
        n *= i
    return n
    
def kempner(x):
    for i in range(1, x+1):
        if fact(i) % x == 0:
            return i

