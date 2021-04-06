
def map_letters(word):
  res = {}
  for x in word:
    res[x] = [idx for idx, i in enumerate(word) if i==x]
  return res

