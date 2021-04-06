
def word_nest(word, nest):
  return min(nest.count(i) for i in nest) - min(word.count(i) for i in word)

