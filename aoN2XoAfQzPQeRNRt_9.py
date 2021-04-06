
def operation(a, b, op):
  a = int(a)
  b = int(b)
  if op == 'divide':
    if b == 0:
      return 'undefined'
    else:
      return str(a // b)
  elif op == 'multiply':
    return str(a * b)
  elif op == 'add':
    return str(a + b)
  elif op == 'subtract':
    return str(a - b)

