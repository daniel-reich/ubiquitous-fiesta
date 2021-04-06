
def word_nest(word, nest):
  count = -1
  while word in nest:
    count += 1
    nest = nest.replace(word,"")
  return count

