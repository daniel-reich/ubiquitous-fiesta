
def no_yelling(phrase):
  for foo in range(len(phrase) - 1,-1,-1):
    if phrase[foo] not in "?!":
      break
  return phrase[:foo + 2]

