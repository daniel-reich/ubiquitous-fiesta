
def happy(n):
  n = sum(int(i)**2 for i in str(n))
  return True if n == 1 else False if n == 4 else happy(n)

