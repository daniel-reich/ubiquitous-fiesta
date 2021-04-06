
def greater_than_one(frac):
  frac = frac.split("/")
  fract = int(frac[0])/int(frac[1])
  if (fract > 1):
    return True
  else:
    return False

