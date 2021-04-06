
def sum_digits(a, b):
  r = 0
  return sum((r + int(el)) for x in range(a,b+1) for el in(str(x)))

