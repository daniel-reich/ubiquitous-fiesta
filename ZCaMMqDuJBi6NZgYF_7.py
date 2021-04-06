
def temp_conversion(c):
  k = round(c+273.15,2)
  return 'Invalid' if k<0 else [round(c*9/5+32,2),k]

