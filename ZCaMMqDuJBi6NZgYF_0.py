
def temp_conversion(C):
  F = round(C*9/5 +32, 2)
  K = C + 273.15
  if K < 0:
    return 'Invalid'
  return [F, K]

