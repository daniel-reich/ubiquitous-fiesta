
def is_prime(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return n!=1
​
def primorial(n):
    count=0
    i=2
    result=1
    while count<n:
        if is_prime(i):
            result*=i
            count+=1
        i+=1
    return result

