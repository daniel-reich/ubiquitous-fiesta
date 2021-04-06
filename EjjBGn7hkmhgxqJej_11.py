
def word_nest(word, nest,c=0):
  if nest == word: return c
  else:
    nest=nest.replace(word,'')
  return word_nest(word,nest,c+1)

