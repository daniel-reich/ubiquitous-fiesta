
def can_complete(initial, word):
  lst = []
  for c in initial:
    try:
      x = word.find(c)
      lst.append(x)
      word = list(word)
      word[x] = '-'
      word = ''.join(word)
    except:
      return False
  return lst == sorted(lst)

