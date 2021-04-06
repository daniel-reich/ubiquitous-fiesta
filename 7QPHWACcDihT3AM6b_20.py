
def can_find(bigrams, words):
  for b in bigrams:
    for w in words:
      if b in w:
        break
    else:
      return False
  return True

