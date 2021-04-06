
def can_find(bigrams, words):
  ctr = 0
  for item in bigrams:
    for word in words:
      if item in word:
        ctr += 1
        break
  return len(bigrams) == ctr

