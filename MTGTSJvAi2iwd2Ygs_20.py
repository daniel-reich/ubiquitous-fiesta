
def valid_division(d):
  if d[-1]!="0":
    return eval(d)%1==0
  else:
    return "invalid"

