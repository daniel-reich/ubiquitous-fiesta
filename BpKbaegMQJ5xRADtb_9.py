
from functools import reduce
​
def is_prime(n):
    if n == 0: return False    
    return len(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if not n % i)))) == 2
​
def is_unprimeable(num):
    if is_prime(num): return 'Prime Input'
    changedNum = []
    for a in range(0, len(str(num)), 1):
        for b in range(0, 10, 1):
            li = list(str(num))
            li[a] = str(b)
            changedNum.append(int("".join(li)))
    changedNum = list(set(changedNum))
    res = []
    for num in changedNum:
        if is_prime(num) == True: res.append(num)
    if res: return sorted(res)
    else: return 'Unprimeable'

