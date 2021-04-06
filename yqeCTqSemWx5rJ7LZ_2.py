
def full_key_name(piece):
  x = piece.split()
  p = piece.split()[-1]
  if p[0].isupper():
    return " ".join(x[:-1]) +" "+ p.capitalize() + " major"
  return " ".join(x[:-1]) +" "+ p.capitalize() + " minor"
  return x[:-1]

