
def smallest(digits, value):
  n = int('1' + '0'*(digits-1))
​
  while n % value:
    n += 1
  return n

