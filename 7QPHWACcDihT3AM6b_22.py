
def can_find(bigrams, words):
  l=[]
  for i in words:
    for k in bigrams:
      if k in i:
        l.append(k)
  return len(set(l))==len(bigrams)

