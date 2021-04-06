
def word_builder(letters, positions):
  return ''.join(x[1] for x in sorted(zip(positions,letters)))

