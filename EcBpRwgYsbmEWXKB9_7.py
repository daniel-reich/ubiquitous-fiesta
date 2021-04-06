
def prime(x):
  if x==2 or x==3 or x==5:
    return True
  return x % 2 != 0 and x % 3 != 0 and x % 5 != 0

