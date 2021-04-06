
def logarithm(base, num):
  i = 0
  for i in range(12):
    if base ** i == num:
      return i
  return 'Invalid'

