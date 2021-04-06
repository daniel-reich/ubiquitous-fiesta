
def full_key_name(piece):
  piece = piece.split()
  last = [' major', ' minor'][piece[-1][0].islower()]
  return ' '.join(piece[:-1] + [piece[-1].capitalize()]) + last

