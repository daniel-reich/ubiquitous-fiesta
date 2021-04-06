
def get_type(value):
  x = str(type(value))
  return eval(x.strip("<class>"))

