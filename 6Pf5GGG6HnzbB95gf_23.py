
def find_factors(n):
  return [x for x in range(1, n//2 + 1) if not n % x] + [n] if n != 0 else []

