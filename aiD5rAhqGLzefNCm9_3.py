
from random import randint
​
def is_prime(n, lmod=1, f=None, pw=None):
    if pw == 0: return lmod == 1
    f, pw = f or randint(2, n -2), pw or n -1
    return is_prime(n, (lmod*f)%n if pw%2 else lmod, (f**2)%n, (pw -pw%2)//2)

