
def temp_conversion(C):
  return [round(C*9/5 +32, 2), round(C + 273.15, 2)] if C + 273.15 >= 0 else 'Invalid'

