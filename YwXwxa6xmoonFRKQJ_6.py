
import math
def josephus(n):
    if n == 0:
        return False
    counter = 0
    while True:
        if 2**counter > n:
            potenz = 2**(counter-1)
            return 2*(n-potenz)
        else:
            counter += 1

