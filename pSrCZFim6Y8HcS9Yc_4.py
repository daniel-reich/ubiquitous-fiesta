
def convert(deg):
  if "C" in deg:
    c = int(deg.split("*")[0])
    c = round((c * 9)/5 + 32)
    return str(int(c)) + "*F"
  elif "F" in deg:
    f = int(deg.split("*")[0])
    f = round((5/9) * (f - 32))
    return str(int(f)) + "*C"
  return "Error"

