
def word_nest(word, nest):
  depth = 0
  while len(nest)>len(word):
    nest = nest.replace(word,'')
    depth+=1
  return depth

