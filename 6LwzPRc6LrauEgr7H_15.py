
def worm_length(worm):
  if len(worm) == 0:
    return "invalid"
  for symbol in worm:
    if symbol != "-":
      return "invalid"
  return str((len(worm)*10)) + " mm."

