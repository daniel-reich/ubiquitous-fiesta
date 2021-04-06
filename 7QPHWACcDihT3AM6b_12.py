
def can_find(bigrams, words):
  lst = []
  for b in bigrams:
    for w in words:
      if b in w and b not in lst:
        lst.append(b)
  return len(lst) == len(bigrams)

