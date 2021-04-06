
def letters(word1, word2):
  w1,w2 = set(word1), set(word2) 
  return [''.join(sorted(w1.intersection(w2))), 
      ''.join(sorted(w1.difference(w2))),
      ''.join(sorted(w2.difference(w1)))]

