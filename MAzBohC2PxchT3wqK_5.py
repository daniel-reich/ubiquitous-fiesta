
def shadow_sentence(a, b):
  if a.count(' ') != b.count(' '):
    return False
​
  words = list(zip(a.split(), b.split()))
  dimns = lambda w1, w2: len(w1) == len(w2)
  letts = lambda w1, w2: all(l not in w2 for l in w1)
​
  return all(letts(w1, w2) and dimns(w1, w2) for w1, w2 in words)

