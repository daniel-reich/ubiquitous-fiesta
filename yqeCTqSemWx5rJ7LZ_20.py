
def full_key_name(piece):
  x = piece.split(" ")
  upper = x[-1][0].isupper()
  x[-1] = x[-1].capitalize()
  if upper:
    x.append("major")
  else:
    x.append("minor")
  return " ".join(x)

