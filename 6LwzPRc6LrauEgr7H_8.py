
def worm_length(worm):
  return "invalid" if set(worm)!={"-"} else "{} mm.".format(worm.count("-")*10)

