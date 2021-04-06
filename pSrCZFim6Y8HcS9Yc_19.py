
def convert(deg):
​
  split_deg = deg.split("*")
​
  if len(split_deg) == 1:
    return "Error"
​
  elif split_deg[-1] == "C":
    return str(round(int(split_deg[0]) * 1.8 + 32)) + "*F"
​
  elif split_deg[-1] == "F":
    return str(round((int(split_deg[0]) - 32) * 5/9)) + "*C"

