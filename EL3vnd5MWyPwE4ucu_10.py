
def fibonacci(n):
  first = 1
  second = 1
  count = 3
  new = first + second
  while count < n:
    first = second
    second = new
    new = first + second
    count += 1
  
  return str(new)

