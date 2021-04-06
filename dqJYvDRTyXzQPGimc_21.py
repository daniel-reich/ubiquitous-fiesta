
def is_unfair_hurdle(hurdles):
  height = len(hurdles)
  spacing = hurdles[-1].count(" ") / (hurdles[-1].count("#") - 1)
  return height >= 4 or spacing < 4

