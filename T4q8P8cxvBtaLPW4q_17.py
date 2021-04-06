
def extract_primes(num):
  
  def isprime(n):
    if n < 2: return False
    for x in range(2, int(n ** .5) + 1):
      if not n % x: return False
    return True
  
  res = []
  for l in range(1, len(str(num)) + 1):
    for s in range(len(str(num)) + 1 - l):
      if isprime(int(str(num)[s:s+l])) and str(num)[s:s+l][0] != "0":
        res += [int(str(num)[s:s+l])]
  return sorted(res)

