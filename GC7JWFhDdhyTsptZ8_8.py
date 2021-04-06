
def sexy_primes(n, limit):
  def is_prime(num):
    for i in range(2, num):
      if num%i == 0:
        return False
    return True
  res = []
  for k in range(2,limit):
    if n ==2 and k < limit-6:
      if is_prime(k) and is_prime(k+6):
        res.append((k, k+6))
    if n ==3 and k < limit-12:
      if is_prime(k) and is_prime(k+6) and is_prime(k+12):
        res.append((k, k+6, k+12))
  return res

