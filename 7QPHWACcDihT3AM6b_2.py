
def can_find(bigrams, words):
  newList = []
  for bigram in bigrams:
      for word in words:
        if bigram in word:
          newList.append(True)
          break
  if len(newList) == len(bigrams):
    return True
  else:
    return False

