
def get_case(txt):
  if txt.islower() == True:
    return 'lower'
  elif txt.isupper() == True:
    return 'upper'
  else:
    return 'mixed'

