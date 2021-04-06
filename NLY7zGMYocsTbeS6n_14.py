
def reverse(arg):
  if type(arg) == bool:
    arg = not arg
    return arg
  return "boolean expected"

