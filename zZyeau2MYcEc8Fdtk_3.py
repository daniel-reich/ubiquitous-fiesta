
def round_number(num, n):
  rem = num % n
  if rem < n - rem:
    return num - rem
  
  return num + n - rem

