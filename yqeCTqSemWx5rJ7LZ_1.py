
def full_key_name(txt):
  piece, note = txt.split()[:-1], txt.split()[-1]
  return '{} {} {}'.format(' '.join(piece), note.title(), ['minor', 'major'][note[0].isupper()])

