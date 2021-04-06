
def sum_digits(a, b):
  s = ""
  for i in range(a, b+1):
    s += str(i)
  s = list(s)
  x = 0
  for i in s:
    x += int(i)
  return x

