
def checkWords(lst):
  lst.sort(key = len)
  w1, w2 = lst[0], lst[1]
  l1, l2 = len(w1), len(w2)
  d = abs(l1-l2)
  if d == 0:
    return sum(1 for i in range(l1) if w1[i] != w2[i]) == 1
  if d == 1:
    return all(i in w2 for i in w1)
  return False
def isWordChain(words):
  return all(checkWords(words[0 + i:2 + i]) for i in range(len(words)-1))

