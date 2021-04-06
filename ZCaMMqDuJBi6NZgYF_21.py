
def temp_conversion(c):
  return [round(c* 9/5 + 32, 2), round(c + 273.15, 2)] if c + 273.15 >= 0 else "Invalid"

