
def word_nest(word, nest):
  for letter in word:
    if word.count(letter) == 1: return nest.count(letter)-1

