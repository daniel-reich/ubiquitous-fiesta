
def valid_division(d):
  try:
    return eval(d)%1==0
  except: return 'invalid'

