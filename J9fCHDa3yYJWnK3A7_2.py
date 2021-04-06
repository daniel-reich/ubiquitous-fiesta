
def is_happy(n):
  new = 0
  for digit in list(str(n)):
      new+=int(digit)**2
  if new==4:
      return False
  elif new==1:
      return True
  else:
      return is_happy(new)

