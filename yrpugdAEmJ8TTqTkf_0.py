
def secret(num):
  x, y = divmod(num, 10)
  return x ** y - x * y

