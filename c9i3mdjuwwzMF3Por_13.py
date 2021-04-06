
import math
​
upDown = {'6': '9', '9': '6', '0': '0', '1': '1', '8': '8'}
​
def isPrime(n):
    n = abs(int(n))
    if n == 2: return True
    if n % 2 == 0: return False
    r = math.sqrt(n)
    x = 3 
    while x <= r:
        if n % x == 0: return False
        x += 2
    return True     
​
def bemirp(n):
    if not isPrime(n):
        return 'C'
    emirp = int(str(n)[::-1])
    if not isPrime(emirp) or emirp == n:
        return 'P'
    bemirp = ""
    for digit in str(n):
        if digit not in upDown:
            return 'E'
        bemirp += upDown[digit]
    bemirp = int(bemirp)
    if not isPrime(bemirp):
        return 'E'
    else:
        return 'B'

