
def worm_length(worm):
  n=0
  for i in worm:
    if i == "-":
      n+=10
    else:
      return "invalid"
  if n == 0:
    return "invalid"
  return str(n) + " mm."

