
def word_nest(word, nest):
  count = 0
  while len(nest) > len(word):
    nest = nest.replace(word, '')
    count += 1
  return count

