
def is_boiling(temp):
​
  t = temp[0:len(temp)-1]
  type = temp[len(temp)-1:]
  if type == "F":
    if int(t) >= 212:
      return True
    else:
      return False
  elif type == "C":
    if int(t) >= 100:
      return True
    else:
      return False

