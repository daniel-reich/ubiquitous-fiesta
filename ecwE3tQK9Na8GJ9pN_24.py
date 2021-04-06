
def little_big(n):
  if n%2==0:
    return 100 * 2**(n//2 - 1)
  return 5 + n//2

