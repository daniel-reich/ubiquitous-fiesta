
def is_pandigital(n):
  return sum(int(x) for x in set(str(n)))==45 and '0' in str(n)

