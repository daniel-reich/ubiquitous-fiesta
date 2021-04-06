
def is_boiling(temp):
  if temp[-1] == "F":
    temp = temp[:-1]
    temp = int(temp)
    if temp >= 212:
      return True
    else:
      return False
  elif temp[-1] == "C":
    temp = temp[:-1]
    temp = int(temp)
    if temp >= 100:
      return True
    else:
      return False

