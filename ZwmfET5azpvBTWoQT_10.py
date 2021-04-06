
def valid_word_nest(word, nest):
  if nest.count(word)!=1: return False
  while word in nest:
    nest=nest.replace(word,'')
  return nest==''

