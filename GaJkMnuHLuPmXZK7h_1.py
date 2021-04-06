
def letters(word1, word2):
  a, b = set(word1), set(word2)
  return [''.join(sorted(i)) for i in (a & b, a - b, b - a)]

