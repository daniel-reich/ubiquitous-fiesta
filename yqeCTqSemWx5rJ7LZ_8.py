
def full_key_name(piece):
  words = piece.split()
  if words[-1].islower(): words[-1] = words[-1].capitalize() + " minor"
  else: words[-1] = words[-1].capitalize() + " major"
  return " ".join(words)

