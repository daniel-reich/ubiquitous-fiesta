
def isPrime(num):
    prime = [2, 3]
    if num in prime:
        return True
    if num<2:
        return False
    for i in range(2, (num+2)//2):
        if num%i ==0:
            return False
    return True
​
def sum_primes(lst):
  if len(lst)==0:
    return None
  lst_index = list(map(isPrime, lst))
  result = [k for i, k in enumerate(lst) if lst_index[i]]
  return sum(result)

