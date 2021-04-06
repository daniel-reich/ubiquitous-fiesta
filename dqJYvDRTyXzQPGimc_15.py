
def is_unfair_hurdle(hurdles):
  if len(hurdles) >= 4:
    return True
  for x in hurdles:
    if (x.count("#")-1)*4 >= len(x):
      return True
  else: return False

