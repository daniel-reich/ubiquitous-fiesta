
def can_find(bigrams, words):
  for i in bigrams:
    k = 0
    for j in words:
      if i in j: 
        k += 1
    if k > 0:
      continue
    else:
      return False
  return True

