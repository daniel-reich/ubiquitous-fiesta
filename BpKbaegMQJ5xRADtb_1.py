
def is_prime(n):
  return n > 1 and all(n % m for m in range(2, int(n ** 0.5) + 1))
​
def is_unprimeable(num):
  if is_prime(num):
    return "Prime Input"
​
  primes = []
  s = str(num)
​
  for d in range(10):
    for i in range(len(s)):
      n = int(s[:i] + str(d) + s[i + 1:])
      if is_prime(n):
        primes.append(n)
​
  return sorted(primes) or "Unprimeable"

