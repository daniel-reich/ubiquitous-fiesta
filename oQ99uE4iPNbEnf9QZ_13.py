
def no_perms_digits(n):
  return len(str(fac(n)))
​
def fac(n):
  return 1 if n==0 else n*fac(n-1)

