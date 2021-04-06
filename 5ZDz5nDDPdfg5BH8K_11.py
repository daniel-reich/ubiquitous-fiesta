
def only_5_and_3(n):
  count = 1
​
  while not n % 5 == 0:
    count *= 3
​
    if (n - count) % 5 == 0:
      n -= count
    
    if n < 0:
      return False
  return True

