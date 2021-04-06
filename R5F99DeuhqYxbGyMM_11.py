
def word_builder(ltr, pos):
  word = ""
  for i in range(0, len(ltr)):
    word += ltr[pos[i]]
  return word

