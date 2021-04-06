
import itertools
def c_fuge(n, k):
    if k == 1 or k == n - 1:
        return False
    elif n == k:
        return True
    lst = get_primes(n)
    return send(lst,n,k)
​
import itertools
def c_fuge(n, k):
    if k == 1 or k == n - 1:
        return False
    if n == k:
        return True
    lst = get_primes(n)
    return send(lst,n,k)
​
def send(lst,n,k):
    a = 0
    cay = 0
    minus = 0
    while a < k:
        a += 1
        for i in itertools.combinations_with_replacement(lst,a):
            if sum(i) == k:
                cay += 1
            if sum(i) == (n - k):
                minus += 1
            if cay >= 1 and minus >= 1:
                return True
    return False
​
def is_prime(x):
    lst = 0
    for i in range(2,x):
        if x % i == 0:
            lst += 1
            break
    return True if lst == 0 else False
​
def get_primes(x):
    lst=[]
    for i in range(2,x):
        if x % i == 0:
            if is_prime(i):
                lst.append(i)
    return lst

