
def word_builder(letters, positions):
  return ''.join([l for i,l in sorted(zip(positions,letters))])

