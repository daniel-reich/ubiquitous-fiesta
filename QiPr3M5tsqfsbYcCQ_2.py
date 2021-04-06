
def square_digits(n):
  x = ''
  for i in str(n):
    x += str(int(i) ** 2)
  return int(x)

