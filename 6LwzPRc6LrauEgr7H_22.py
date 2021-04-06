
def worm_length(worm):
  if not worm or len(set(worm)) != 1:
    return "invalid"
  res = len([elem for elem in worm if elem == '-'])
  return "{} mm.".format(res*10)

