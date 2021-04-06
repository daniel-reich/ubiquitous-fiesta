
def no_perms_digits(n):
  return len(str(get_factorial(n)))
    
def get_factorial(n):
  if n == 0:
    return 1
  else:
    return n * get_factorial(n-1)

