
def letters(word1, word2):
  shared = ''.join(sorted(set(x for x in word1 if x in word2)))
  w1 = ''.join(sorted(set(x for x in word1 if x not in word2)))
  w2 = ''.join(sorted(set(x for x in word2 if x not in word1)))
  return [shared,w1,w2]

