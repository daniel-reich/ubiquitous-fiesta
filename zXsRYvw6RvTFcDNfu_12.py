
from math import sqrt
​
def prime_factorization(number):
​
    lst = []
    n = round(sqrt(number))
​
    while number != 1:
        for i in range(2, n+1):
            if number % i == 0:
                number /= i
                lst.append(i)
                break
            if i == n:
                lst.append(int(number))
                number = 1
    return lst
​
def to_destinct(fac):
    lst = []
    for e in fac:
        if not e in lst:
            lst.append(e)
​
    return lst
​
def ruth_aaron(n):
​
    count = 0
    case_1 = prime_factorization(n - 1)
    case_2 = prime_factorization(n + 1)
    n_fac = prime_factorization(n)
​
    if sum(to_destinct(case_1)) == sum(to_destinct(n_fac)):
        name = "Aaron"
        count += 1
    
    if sum(case_1) == sum(n_fac):
        name = "Aaron"
        count += 2
​
    if sum(to_destinct(case_2)) == sum(to_destinct(n_fac)):
        name = "Ruth"
        count += 1
    
    if sum(case_2) == sum(n_fac):
        name = "Ruth"
        count += 2
​
    if count == 0:
        return False
    else:
        return [name, count]

