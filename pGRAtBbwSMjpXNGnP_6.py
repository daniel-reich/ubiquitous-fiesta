
def is_sorted(words, alphabet):
  def conv(w):
    return [alphabet.index(l) for l in w]
  
  return words == sorted(words, key = conv)

