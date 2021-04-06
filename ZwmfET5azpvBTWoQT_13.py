
def valid_word_nest(word, nest):
  while True:
    if nest.count(word) != 1:
      return False
    elif nest == word:
      return True
    else:
      nest = nest.replace(word,"")

