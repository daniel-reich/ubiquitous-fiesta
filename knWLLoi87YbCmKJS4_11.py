
def happy(n):
  for i in range(10):
    preN = n
    n = sum(int(i)**2 for i in str(n))
    if n==1:
      return True
  return False

