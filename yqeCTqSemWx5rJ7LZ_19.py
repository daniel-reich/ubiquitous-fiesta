
def full_key_name(piece):
  a = piece.split(' ')
  if a[-1].islower():
    return ' '.join(a[:-1]) + ' ' + a[-1].title() + ' minor'
  else:
    return ' '.join(a[:-1]) + ' ' + a[-1].title() + ' major'

