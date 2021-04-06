
def word_builder(letters, positions):
  return ''.join(letters[positions.index(i)] for i in range(len(letters)))

