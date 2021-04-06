
def getPrimes(upperLimit):
  primes = []
  for n in range(2, upperLimit+1):
    if len([p for p in primes if n % p == 0]) == 0:
      primes.append(n)
  
  return primes
​
def extract_primes(num):
  primes = getPrimes(num)
  s = str(num)
  
  ans = []
  
  for i in range(1, len(s)+1):
    for j in range(0, len(s) + 1 - i):
      if s[j] != "0":
        slice = int(s[j:j+i])
        if slice in primes:
          ans.append(slice)
  
  return sorted(ans)

