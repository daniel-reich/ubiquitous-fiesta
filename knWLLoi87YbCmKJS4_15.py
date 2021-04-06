
def happy(n):
  while n not in {1, 4}:
    n = sum(int(i)**2 for i in str(n))
  return n == 1

