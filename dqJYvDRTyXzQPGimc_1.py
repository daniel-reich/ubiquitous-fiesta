
def is_unfair_hurdle(hurdles):
  return len(hurdles) > 3 or len(hurdles[0].split('#')[1]) < 4

