
def equal_slices(total, people, each):
  if people == 0 or each == 0:
    return True
  elif (total >= people * each):
    return True
  else:
    return False

