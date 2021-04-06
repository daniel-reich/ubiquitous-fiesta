
# without iteration
def smallest(digits, value):
  if value == 1:
    return 10**(digits - 1)
  return value + int(10**(digits - 1) / value) * value

