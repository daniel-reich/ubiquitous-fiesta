
def full_key_name(piece):
  piece = piece.split(" ")
  key = piece[-1]
  keyup = key[0].upper() + key[1:]
  if key[0].isupper():
    piece[-1] = keyup + " major"
  else:
    piece[-1] = keyup + " minor"
  return " ".join(piece)

