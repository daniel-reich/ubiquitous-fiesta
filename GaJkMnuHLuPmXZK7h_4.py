
def letters(word1, word2):
  s_set = set(word1).intersection(set(word2))
  dif_1 = set(word1).difference(set(word2))
  dif_2 = set(word2).difference(set(word1))
  return [''.join(sorted(list(s_set))), ''.join(sorted(list(dif_1))), ''.join(sorted(list(dif_2)))]

