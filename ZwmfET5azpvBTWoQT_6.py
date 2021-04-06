
def valid_word_nest(word, nest):
  count = 0
  while nest != word:
    if nest.count(word) != 1:
      return False
​
    try:
      ndx = nest.index(word)
      nest = nest[:ndx] + nest[ndx+len(word):]
      count += 1
    except:
      return False
  return True

