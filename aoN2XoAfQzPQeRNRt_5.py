
def operation(a, b, op):
  if op == 'add':
    return str(int(a)+int(b))
  if op == 'subtract':
    return str(int(a)-int(b))
  if op == 'multiply':
    return str(int(a)*int(b))
  if op == 'divide':
    if b == '0':
      return 'undefined'
    return str(int(int(a)/int(b)))

