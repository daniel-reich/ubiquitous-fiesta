
def smallest(digits, value):
  for i in range (10**(digits-1),10**digits-1):
    if i%value==0:
      return i

