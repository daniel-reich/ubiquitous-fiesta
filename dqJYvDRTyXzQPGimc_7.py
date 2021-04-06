
def is_unfair_hurdle(hurdles):
  return len(hurdles) >= 4 or hurdles[0][1:].index('#') < 4

