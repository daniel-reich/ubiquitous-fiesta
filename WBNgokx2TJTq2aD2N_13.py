
def smallest(digits, value):
  n = 10**(digits-1)
  while n%value and n < 10**digits:
    n+=1
  return n

