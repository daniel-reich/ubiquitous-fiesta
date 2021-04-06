
def fibonacci(n):
  first = 1
  second = 2
  count = 0
  for i in range(0, n):
    if i<=2:
      i = 0
    else:
      total = first + second
      first = second
      second = total
  return str(total)

