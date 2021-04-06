
def word_nest(word, nest):
  total = 0
  w = len(word)
  while w < len(nest):
    w += len(word)
    total += 1
  return total

