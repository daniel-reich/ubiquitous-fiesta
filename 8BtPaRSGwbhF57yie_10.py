
def match_houses(step):
  if step == 1:
    return 6
  elif step == 0:
    return 0
  else:
    return 6 + ((step - 1) * 5)

