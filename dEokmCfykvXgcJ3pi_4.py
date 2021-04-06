
def first_arg(*args):
  return args[0] if len(args) > 0 else None
​
def last_arg(*args):
  return args[len(args)-1] if len(args) > 0 else None

