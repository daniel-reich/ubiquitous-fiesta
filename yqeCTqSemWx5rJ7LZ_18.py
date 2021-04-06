
def full_key_name(piece):
  words = piece.split()
  key = words[-1]
  if key[0].islower():
    return ' '.join(words[:-1]) + ' ' + key.title() + ' minor'
  else:
    return ' '.join(words[:-1]) + ' ' + key.title() + ' major'

