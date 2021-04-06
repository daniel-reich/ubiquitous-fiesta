
def doubled_pay(n):
  if n == 1:
    return 1
  else:
    return 2**(n-1) + doubled_pay(n-1)

