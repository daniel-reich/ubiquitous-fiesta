
def is_unfair_hurdle(hurdles):
  if len(hurdles) > 3: return True
  if len(hurdles[0].split('#')[1]) < 4: return True
  return False

