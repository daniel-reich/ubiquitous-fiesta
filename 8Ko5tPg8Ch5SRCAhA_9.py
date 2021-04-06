
def fibonacci(num):
  if num == 0 or num == 1:
    return 1
  
  a = 0
  b = 1
  c = 0
  for i in range(num):
    c = a + b
    a = b
    b = c
  return c

