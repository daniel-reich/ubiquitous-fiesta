
def can_find(bigrams, words):
  lst = []
  for x in words:
    for y in bigrams:
      if y in x and y not in lst:
        lst.append(y)
      else:
        continue
  return len(lst) == len(bigrams)

