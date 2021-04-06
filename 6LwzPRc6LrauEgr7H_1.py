
def worm_length(worm):
  if worm == "":
    return "invalid"
  for x in worm:
    if x != "-":
      return "invalid"
  return str(len(worm) * 10) + " mm."

