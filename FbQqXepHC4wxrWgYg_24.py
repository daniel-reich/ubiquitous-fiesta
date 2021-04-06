
def prime_divisors(num):
    lst = []
    lst1 = []
    c = 0
    for i in range(2, int(num)):
        if num % i == 0:
            lst.append(i)
    for j in lst:
        if prime(j) or j == 2:
            lst1.append(j)
    return lst1
​
def prime(num):
    if num % 2 == 0:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

