
def worm_length(worm):
  x = 0
  if len(worm) == 0: return "invalid"
  for i in worm:
    if i != "-": return "invalid"
  for j in worm:
    if j == "-": x += 10
  return "{} mm.".format(x)

