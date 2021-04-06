
def word_nest(word, nest):
  count = 0
  while nest != word:
    nest = nest.replace(word, '')
    count += 1
  return count

