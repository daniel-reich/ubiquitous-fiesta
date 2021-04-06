
def prime_in_range(n1, n2):
  return any(n > 1 and all(n % m for m in range(2, int(n ** 0.5) + 1)) for n in range(n1, n2 + 1))

