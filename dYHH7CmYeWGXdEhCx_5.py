
def word_builder(letters, positions):
  return ''.join(letter for _,letter in sorted(zip(positions,letters)))

