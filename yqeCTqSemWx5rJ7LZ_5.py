
def full_key_name(piece):
  piece=piece.split()
  if piece[-1].islower(): piece.append('minor')
  else: piece.append('major')
  piece[-2]=piece[-2].title()
  return ' '.join(piece)

