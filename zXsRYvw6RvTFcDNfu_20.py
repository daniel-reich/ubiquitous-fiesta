
def ruth_aaron(n):
  smoler = n-1
  larger = n + 1
  def is_prime(k):
    for j in range(2, k):
      if k%j == 0:
        return False
    return True
  def primes(num):
    facts = []
    for i in range(2, num+1):
      if num %i == 0:
        if is_prime(i):
          count = 0
          t = num
          while t%i == 0:
            count += 1
            t /= i
          facts.extend([i]*count)
    return facts
  p1 = sum(primes(smoler))
  p2 = sum(primes(n))
  p3 = sum(primes(larger))
  s1 = sum(list(set(primes(smoler))))
  s2 = sum(list(set(primes(n))))
  s3 = sum(list(set(primes(larger))))
  if p1 == p2 and s1 == s2:
    return ['Aaron', 3]
  if p2 == p3 and s2 == s3:
    return ['Ruth', 3]
  if p1 == p2:
    return ['Aaron', 2]
  if p2 == p3:
    return ['Ruth', 2]
  if s1 == s2:
    return ['Aaron', 1]
  if s2 == s3:
    return ['Ruth', 1]
  return False

