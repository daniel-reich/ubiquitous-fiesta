
def temp_conversion(celsius):
  F = celsius*9/5 +32
  K = celsius + 273.15
  return [round(F, 2), round(K, 2)] if K >= 0 else "Invalid"

