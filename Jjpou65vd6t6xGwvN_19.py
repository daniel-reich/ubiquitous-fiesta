
def get_case(txt):
  
  if txt.istitle():
    return 'mixed'
      
  elif txt.isupper():
    return 'upper'
      
  elif txt.islower():
    return 'lower'

