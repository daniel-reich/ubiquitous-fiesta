
def letters(word1, word2):
  w1 = set(list(word1))
  w2 = set(list(word2))
  intersect = sorted(w1.intersection(w2))
  unique1 = sorted(w1.difference(intersect))
  unique2 = sorted(w2.difference(intersect))
  return ["".join(intersect), "".join(unique1), "".join(unique2)]

