
def valid_division(d):
  try:
    x = eval(d)
  except:
    return "invalid"
    
  if x>=0:
    if divmod(x,1)[1] == 0:
      return True
    else:
      return False

