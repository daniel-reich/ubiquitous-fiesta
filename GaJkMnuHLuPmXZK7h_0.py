
def letters(word1, word2):
  s1, s2 = set(word1), set(word2)
  return [''.join(sorted(i)) for i in [s1&s2, s1-s2, s2-s1]]

