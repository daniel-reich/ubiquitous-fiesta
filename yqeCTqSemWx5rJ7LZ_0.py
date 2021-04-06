
def full_key_name(piece):
  a, b = piece.rsplit(' ', 1)
  return '{} {} {}'.format(a, b.title(), 'major' if b[0].isupper() else 'minor')

