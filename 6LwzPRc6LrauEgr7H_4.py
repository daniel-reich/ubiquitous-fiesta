
def worm_length(worm):
  if any(x!="-" for x in worm) or not worm:
    return "invalid"
  return "{} mm.".format(len(worm)*10)

