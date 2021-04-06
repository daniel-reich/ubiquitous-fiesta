
def temp_conversion(celsius):
  return [round(celsius * 9 / 5 + 32, 2), round(celsius + 273.15, 2)] if round(celsius + 273.15, 2) > 0 else "Invalid"

