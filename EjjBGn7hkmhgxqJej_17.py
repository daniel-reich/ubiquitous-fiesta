
def word_nest(word, nest):
  x = 0
  while len(nest)>0:
    nest = nest.replace(word,'')
    x += 1
  return x-1

