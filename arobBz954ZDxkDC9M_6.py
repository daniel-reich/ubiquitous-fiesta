
def prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False
    
def next_prime(x):
    if prime(x):
        return x
    else:
        for i in range(x, x+50):
            if prime(i):
                return i

