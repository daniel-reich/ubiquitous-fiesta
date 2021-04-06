
def only5and3(n):
  if n == 3 or n == 5:
    return True
​
  if n <= 0:
    return False
​
  return only5and3(n - 5) or only5and3(n / 3)

