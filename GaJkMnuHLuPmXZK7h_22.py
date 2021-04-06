
def letters(word1, word2):
  w1 = set(word1)
  w2 = set(word2)
  shared = []
  w1_list = []
  w2_list = []
  for c in w1 :
    if c in w2 :
      shared.append(c)
    else :
      w1_list.append(c)
  for c in w2 :
    if c not in w1:
      w2_list.append(c)
  shared.sort()
  w1_list.sort()
  w2_list.sort()
  return [''.join(shared),''.join(w1_list), ''.join(w2_list)]

