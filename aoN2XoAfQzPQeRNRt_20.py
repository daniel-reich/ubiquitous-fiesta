
def operation(a, b, op):
  if op == 'add':
    add = int(a) + int(b)
    return str(add)
  elif op == 'subtract':
    if a == b:
      return "0"
    else:
      subtract =  int(a) - int(b)
      return str(subtract)
  elif op == 'multiply':
    multiply = int(a) * int(b)
    return str(multiply)
  elif op == 'divide':
    if b == "0":
      return "undefined"
    elif a == "0":
      return "0"
    else:
      divide = int(int(a)/int(b))
      return str(divide)

