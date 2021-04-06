
def valid_word_nest(word, nest):
  if word not in nest: return False
  if nest == word: return True
  r = nest.index(word)
  rr = nest.rindex(word)
  if r-rr: return False
  return valid_word_nest(word, nest[:r]+nest[r+len(word):])

