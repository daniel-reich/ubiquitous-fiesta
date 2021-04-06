
def no_perms_digits(n):
  return len(str(factorial(n)))
  
def factorial(n):
  return 1 if not n else n * factorial(n-1)

