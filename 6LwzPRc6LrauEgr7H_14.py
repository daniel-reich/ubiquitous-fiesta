
def worm_length(worm):
  return "invalid" if set(worm) == {''} or set(worm) != {'-'} else "{} mm.".format(len(worm)*10)

