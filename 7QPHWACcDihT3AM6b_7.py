
def can_find(bigrams, words):
  total = 0
  for item in bigrams:
    f1 = 0
    for word in words:
      if item in word:
        f1 += 1
    if f1 > 0:
      total += 1
  return(total == len(bigrams))

