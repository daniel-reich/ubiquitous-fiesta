
def word_builder(letters, positions):
  word = ['_']*len(letters)
  for l, p in zip(letters, positions):
    word[p] = l
  return ''.join(word)

