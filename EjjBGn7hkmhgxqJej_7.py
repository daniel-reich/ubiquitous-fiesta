
def word_nest(word, nest):
  for i in set(word):
    if word.count(i) == 1:
      return nest.count(i)-1

