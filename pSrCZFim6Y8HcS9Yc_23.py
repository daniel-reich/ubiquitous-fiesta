
def convert(deg):
  try:
    t, unit = deg.split("*")
  except:
    return "Error"
  t = int(t)
  if unit == "C":
    return str(round(t * 1.8 + 32)) + "*F"
  if unit == "F":
    return str(round((t - 32) / 1.8)) + "*C"

