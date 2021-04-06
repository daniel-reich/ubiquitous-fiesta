
def is_sastry(n):
  j = str(n) + str(n+1)
  return int(j)**(1/2) == int(int(j)**(1/2))

