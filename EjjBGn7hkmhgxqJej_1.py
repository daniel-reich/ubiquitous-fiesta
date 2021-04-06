
def word_nest(word, nest):
  c = -1
  while nest:
    u = nest.index(word)
    nest = nest[:u] + nest[u + len(word):]
    c += 1
  return c

