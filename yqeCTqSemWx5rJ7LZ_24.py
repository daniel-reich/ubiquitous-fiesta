
def full_key_name(piece):
  note = piece[-2:].strip()
  if len(note) > 1:
    if note[0].islower():
      return piece[:-2] + piece[-2].upper() + piece[-1] + ' minor'
    else:
      return piece[:-2] + piece[-2].upper() + piece[-1] + ' major'
​
  else:
    if note[-1].islower():
      return piece[:-1] + piece[-1].upper() + ' minor'
    else:
      return piece[:-1] + piece[-1].upper() + ' major'

