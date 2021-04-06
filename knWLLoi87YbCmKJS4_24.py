
def happy(n):
  new = sum([int(i)**2 for i in str(n)])
  return new == 1 or new == 10 or new == 82

