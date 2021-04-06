
def valid_division(d):
  try:
    return int(eval(d)) == float(eval(d))
  except:
    return 'invalid'

