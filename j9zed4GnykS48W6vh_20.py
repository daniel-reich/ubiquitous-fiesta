
def digits(n):
  digs = 0
  j = 0
  while n >= 10**j:
    j += 1
    digs += 9*j*10**(j-1) if n >= 10**j else (n-10**(j-1))*j
  return digs

