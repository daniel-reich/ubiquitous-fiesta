
def word_nest(word, nest):
  nesting = -1
  while nest.count(word) > 0:
    nest = nest.replace(word, '')
    nesting += 1
  return nesting

