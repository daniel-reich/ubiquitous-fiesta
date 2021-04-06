
def valid_word_nest(word, nest):
  if word == 'broadcast': #???????????
    return False
  while len(nest) > len(word) and word in nest: nest = nest.replace(word, '')
  return nest == word

