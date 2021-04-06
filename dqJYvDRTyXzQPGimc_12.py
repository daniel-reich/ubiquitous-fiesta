
def is_unfair_hurdle(hurdles):
  if len(hurdles) >= 4:
    return True
  else:
    if (len(hurdles[0])-hurdles[0].count("#"))/(hurdles[0].count("#")-1) < 4:
      return True
    else:
      return False

