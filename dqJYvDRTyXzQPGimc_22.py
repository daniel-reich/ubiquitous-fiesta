
def is_unfair_hurdle(hurdles):
  return len(hurdles) >= 4 or len(hurdles[0].split("#")[1]) < 4

