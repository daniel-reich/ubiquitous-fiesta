
def is_unfair_hurdle(hurdles):
  if len(hurdles) >= 4:
    return True
  else:
    h = hurdles[0].count("#")
    s = 0
    for k in range(0, len(hurdles[0])):
      if hurdles[0][k].isspace():
        s += 1
    if s/(h-1) >= 4:
      return False
    else:
      return True

