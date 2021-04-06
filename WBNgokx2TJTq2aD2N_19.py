
def smallest(digits, value):
  first = int(pow(10, digits - 1))
  while first % value != 0:
    first += 1
  return first

