
def is_prime(primes, num, left=0, right=None):
  mid = primes[int(len(primes)/2)]
​
  if mid == num:
      return "yes"
  
  if (len(primes) == 1):
      return "no"
  
  if mid < num:
    return is_prime(primes[int(len(primes)/2): len(primes)], num, 0, None )
    
  if mid > num:
        return is_prime(primes[0:int(len(primes)/2)], num, 0, None )

