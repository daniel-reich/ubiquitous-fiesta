
def first_arg(*args):
  if not args:
    return None
  return args[0]
​
def last_arg(*args):
  if not args:
    return None
  return args[-1]

