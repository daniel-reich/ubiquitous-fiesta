
def valid_word_nest(word, nest):
  while nest.count(word)==1:
    nest=nest.replace(word,'')
  return nest==''

