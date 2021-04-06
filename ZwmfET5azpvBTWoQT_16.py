
def valid_word_nest(word, nest):
  while nest:
    if nest.count(word) > 1:
      return False
    
    new_nest = nest.replace(word, '')
    if new_nest == nest:
      return False
    else:
      nest = new_nest
  
  return True

