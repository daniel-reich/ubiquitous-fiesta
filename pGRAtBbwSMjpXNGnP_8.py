
def is_sorted(words, alphabet):
  idx=lambda x: tuple(alphabet.index(x[i]) for i in range(len(x)))
  return sorted(words, key=lambda x:idx(x))==words

