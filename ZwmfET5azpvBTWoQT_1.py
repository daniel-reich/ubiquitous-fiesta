
def valid_word_nest(word, nest):
  while word in nest and nest.count(word)==1:
    nest = nest.replace(word,'')
  return not nest

