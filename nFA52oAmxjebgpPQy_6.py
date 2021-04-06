
def char_index(word, char):
  g = [i for i, a in enumerate(word) if a == char]
  if len(g) > 1:
    return [min(g), max(g)]
  elif len(g) == 1:
    return g * 2
  else:
    return None

