
def basic_calculator(a, o, b):
  if(o == "+"):
    return a + b
  if(o == "-"):
    return a - b
  if(o == "/" and a != 0 and b != 0):
    return a / b
  if(o == "*"):
    return a * b
  else:
    return None

