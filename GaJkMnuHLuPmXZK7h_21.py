
def letters(word1, word2):
  a = set(word1)
  b = set(word2)
  
  x = ''.join(sorted(a.intersection(b)))
  y = ''.join(sorted(a.difference(b)))
  z = ''.join(sorted(b.difference(a)))
  return [x, y, z]

