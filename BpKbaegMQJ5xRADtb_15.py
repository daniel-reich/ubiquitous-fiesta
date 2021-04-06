
def is_prime(n):
  for i in range(2, n // 2 + 1):
    if not n % i:
      return False
  return True if n >= 2 else False
def is_unprimeable(n):
  if is_prime(n):
    return "Prime Input"
  primes = []
  for i in range(len(str(n))):
    for j in range(10):
      new = bytearray(str(n), "utf-8")
      new[i] = ord(str(j))
      if is_prime(int(new.decode())):
        primes.append(int(new.decode()))
  return sorted(primes) if primes else "Unprimeable"

