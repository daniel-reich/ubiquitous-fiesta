
def equal_slices(total, people, each):
  if people == 0:
    return True
  else: return people * each <= total

