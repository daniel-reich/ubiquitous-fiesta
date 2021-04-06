
def map_letters(word):
  result = {}
  if len(word) == 0:
    return {}
  lst = []
  for y in word:
    result[y] = []
  for x in word:
      a = word.index(x)
      for z in range(word.count(x)):
        a = word.index(x,a,len(word))
        result[x].append(a)
        a +=1
      result[x] = sorted(list(dict.fromkeys(result[x])))
  return result

