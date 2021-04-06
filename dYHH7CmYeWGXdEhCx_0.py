
def word_builder(letters, positions):
  return ''.join(letter for pos, letter in sorted(zip(positions, letters)))

