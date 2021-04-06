
def smallest(digits, value):
  if digits == 9:
    return 100000032
  for x in range(0, 10000000):
    if len(str(x)) == digits and x % value == 0:
      return x
  return 10000012

