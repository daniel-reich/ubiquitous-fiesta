
import math
​
def getPrimeFactors(n):
    arr = []
    while n % 2 == 0:
        arr.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            arr.append(i)
            n = n / i
    if n > 2:
        arr.append(int(n))
    return arr
​
​
def ruth_aaron(n):
    a = getPrimeFactors(n)
    b = getPrimeFactors(n + 1)
    c = getPrimeFactors(n - 1)
    name = ""
    if sum(a) == sum(b):
        name = "Ruth"
        if sum(set(a)) == sum(set(b)):
            type = 3
        else:
            type = 2
    if sum(set(a)) == sum(set(b)) and sum(a) != sum(b):
        name = "Ruth"
        type = 1
    elif sum(a) == sum(c):
        name = 'Aaron'
        if sum(set(a)) == sum(set(c)):
            type = 3
        else:
            type = 2
    if sum(set(a)) == sum(set(c)) and sum(a) != sum(c):
        name = "Aaron"
        type = 1
    if name == '': return False
    return [name, type]

