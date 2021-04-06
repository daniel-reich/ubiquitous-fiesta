
def letters(word1, word2):
  
  shared = sorted(set(word1) & set(word2))
  uniq1 = sorted(set(word1) - set(word2))
  uniq2 = sorted(set(word2) - set(word1))
  
  return [''.join(shared), ''.join(uniq1), ''.join(uniq2)]

