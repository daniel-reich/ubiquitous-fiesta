
def basic_calculator(a, o, b):
  if o == "+":
    return a + b
  elif o == "-":
    return a - b
  elif o == "*":
    return a * b
  elif o == "/":
    if b == 0:
      return None
    else:
      return a / b
  else:
    return None

