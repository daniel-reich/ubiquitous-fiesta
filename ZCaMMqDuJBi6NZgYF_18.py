
def temp_conversion(c):
  f = round(c*9/5 +32,2)
  k = round(c + 273.15,2)
  return [f,k] if k>0 else 'Invalid'

