
def valid_word_nest(word, nest):
  prePos = len(word)
  while word in nest:
    pos = nest.find(word)
    if pos == prePos:
      return False
    prePos = pos
    nest = nest.replace(word,"", 1)
  return not nest

