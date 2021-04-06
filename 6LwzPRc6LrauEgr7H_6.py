
def worm_length(worm):
  if worm == "" or worm.count("-") != len(worm):
    return "invalid"
  return str(len(worm)*10) + " mm."

