
def word_builder(ltr, pos):
  word = [ltr[pos[i]] for i in range(len(ltr))]
  return "".join(word)

