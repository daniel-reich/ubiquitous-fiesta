
def smallest(digits, value):
  n=10**(digits-1)
  while n%value:
    n+=1
  return n

