
def first_arg(*args):
  if len(args) == 0:
    return None
  else:
    return args[0]
  
​
def last_arg(*args):
  if len(args) == 0:
    return None
  else:
    return args[-1]

