
def root_digit(n):
  while len(str(n))>1:
    n = sum(int(x) for x in str(n))
  return n

