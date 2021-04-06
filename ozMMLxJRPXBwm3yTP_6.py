
def is_factorial(n):
    x = 1
    for i in range(1,n+1):
        if i*x == n:
            return True
            break
        else:
            x = x*i
    return False

