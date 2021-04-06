
def full_key_name(piece):
  words = piece.split()
  if words[-1][0].islower():
    words[-1] = words[-1].title()
    words += ["minor"]
  else:
    words += ["major"]
  return " ".join(word for word in words)

