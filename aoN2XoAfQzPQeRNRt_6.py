
def operation(a, b, op):
  if op == 'subtract':
    return str(int(a)-int(b))
  elif op == 'add':
    return str(int(a)+int(b))
  elif op == 'multiply':
    return str(int(a)*int(b))
  else:
    if a != '0' and b != '0':
      return str(int(int(a)/int(b)))
    elif a == '0':
      return '0'
    else:
      return 'undefined'

