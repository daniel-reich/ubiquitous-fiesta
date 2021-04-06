
def char_index(word, char):
  a = [n for n in range(len(word)) if word[n] == char]
  return [a[0], a[-1]] if len(a) > 0 else None

