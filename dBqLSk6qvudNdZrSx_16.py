
def is_boiling(temp):
  if temp[-1] == 'F' and int(temp[:-1]) >= 212:
    return True
  elif temp[-1] == 'C' and int(temp[:-1]) >= 100:
    return True
  else:
    return False

