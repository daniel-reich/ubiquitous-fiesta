
def full_key_name(piece):
  piece=piece.split()
  return ' '.join(piece)+' major' if piece[-1][0].isupper() else ' '.join(piece[:-1])+' '+piece[-1].capitalize()+' minor'

