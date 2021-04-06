
def full_key_name(piece):
  pi = piece.split()
  if pi[-1].istitle():return piece + ' major'
  else:
    pi[-1] = pi[-1].capitalize()
    return ' '.join(pi) + ' minor'

