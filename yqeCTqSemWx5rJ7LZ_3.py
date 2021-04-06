
def full_key_name(piece):
  last_word = piece.split()[-1]
  if last_word[0].islower():
    return ' '.join(piece.split()[:-1]) + " " + piece.split()[-1].title() + ' minor'
  return ' '.join(piece.split()[:-1]) + " " + piece.split()[-1].title() + ' major'

