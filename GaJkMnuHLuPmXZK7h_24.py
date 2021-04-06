
def letters(word1, word2):
  a = "".join(sorted([i for i in set(word1) if i in word2]))
  b = "".join(sorted([i for i in set(word1) if not i in word2]))
  c = "".join(sorted([i for i in set(word2) if not i in word1]))
  return [a,b,c]

