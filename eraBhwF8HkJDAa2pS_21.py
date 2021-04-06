
def pirates_killed(gold, tolerance):
  return any(max(gold) - g > t for g, t in zip(gold, tolerance))

