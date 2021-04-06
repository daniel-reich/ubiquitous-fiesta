
def word_builder(letters, positions):
  word = ""
  a = sorted(zip(letters, positions), key = lambda x : x[1])
  for l, p in a:
    word += l
  return word

