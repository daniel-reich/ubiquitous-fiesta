
def valid_word_nest(word, nest):
  return word == nest or nest.count(word) == 1 and valid_word_nest(word, nest.replace(word, ""))

