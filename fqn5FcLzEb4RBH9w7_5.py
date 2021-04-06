
def equal_slices(total, people, each):
  if people == 0:
    return True
  else:
    if total >= (people * each):
      return True
    else:
      return False

