
def temp_conversion(celsius):
  F = round(celsius * 9/5 + 32, 2)
  K = round(celsius + 273.15, 2)
  
  if celsius < -273.13:
    return "Invalid"
  
  return [F, K]

