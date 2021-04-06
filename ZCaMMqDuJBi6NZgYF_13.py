
def temp_conversion(C):
  if C < -273.13: return 'Invalid'
  return [round((C*9/5 +32),2), round((C + 273.15),2)]

