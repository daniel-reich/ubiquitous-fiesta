
def is_unfair_hurdle(hurdles):
  if len(hurdles) > 3:
    return True
  if hurdles[0][1:5] != "    ":
    return True
  return False

