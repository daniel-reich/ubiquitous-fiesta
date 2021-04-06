
def is_pandigital(n):
  return sorted(set(str(n))) == [str(n) for n in range(10)]

