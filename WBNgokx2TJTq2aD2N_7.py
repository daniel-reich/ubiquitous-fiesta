
def smallest(digits, value):
  num = value
  while len(str(num))<digits:
    num+=value
  return num

