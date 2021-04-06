
def temp_conversion(celsius):
  f = round(celsius*9/5+32,2)
  k = round(celsius + 273.15,2)
  return [f, k] if k > 0 else 'Invalid'

