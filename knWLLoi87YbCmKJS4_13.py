
def happy(n):
  while True:
    total = sum(int(x)**2 for x in str(n))
    if '4' in str(total):
      return False
    elif total == 1:
      return True
    n = total
  return True

