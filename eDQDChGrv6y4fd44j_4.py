
def can_put(txt, dim):
  words = txt.split()
  row, col = dim
  for r in range(row):
    long = col
    while words and long >= len(words[0]):
      long -= len(words[0]) + 1
      words.pop(0)
  return not words

