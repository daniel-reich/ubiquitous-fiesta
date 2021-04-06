
def is_factorial(x):
  def factorial(n):
    f, count = 1, 0
    while count < n:
      count += 1
      f *= count
    return f
  y, lst = 0, []
  while y < x:
    y += 1
    lst += [y]
  return x in [factorial(i) for i in lst]

