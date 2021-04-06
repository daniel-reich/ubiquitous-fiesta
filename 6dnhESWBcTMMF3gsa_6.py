
def stupid_addition(a, b):
  if type(a) == str and type(b) == str:
    return int(a)+int(b)
  elif type(a) == int and type(b) == int:
    return str(a)+str(b)
    return "None"

