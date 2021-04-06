
def eratosthenes(num):
  return [x for x in range(num+1) if isPrime(x)]
​
​
def isPrime(a):
    return sum([1 for x in range(2,a+1) if a%x==0])==1

