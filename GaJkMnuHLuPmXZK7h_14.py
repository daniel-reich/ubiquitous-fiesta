
def letters(word1, word2):
  intersection = ''.join(x for x in sorted(set(word1).intersection(set(word2))))
  u1 = ''.join(sorted([x for x in set(word1) if x not in intersection]))
  u2 = ''.join(sorted([x for x in set(word2) if x not in intersection]))
  return [intersection, u1, u2]

