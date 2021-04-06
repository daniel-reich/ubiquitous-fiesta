
def first_arg(*args):
  if args:
    return args[0]
  return None
​
def last_arg(*args):
  if args:
    return args[len(args)-1]
  return None

