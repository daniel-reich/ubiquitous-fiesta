
def operation(a, b, op):
  if op == "add":
    return str(eval(a + " + " + b))
  elif op == "subtract":
    return str(eval(a + " - " + b))
  elif op == "multiply":
    return str(eval(a + " * " + b))
  else:
    if b == "0":
      return "undefined"
    else:
      return str(int(eval(a + " / " + b)))

