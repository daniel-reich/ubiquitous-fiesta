
def first_arg(*vartuple):
  if len(vartuple) > 0:
    return vartuple[0]
  else:
    return None
​
def last_arg(*vartuple):
  if len(vartuple) > 0:
    return vartuple[-1]
  else:
    return None

