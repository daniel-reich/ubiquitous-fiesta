
def word_nest(word, nest):
  l = -1
  while nest:
    nest = ''.join(nest.split(word))
    l+=1
  return l

