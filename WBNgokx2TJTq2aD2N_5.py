
def smallest(digits, value):
  n = 10 ** (digits - 1)
  while True:
    if n % value:
      n += 1
    else:
      return n

