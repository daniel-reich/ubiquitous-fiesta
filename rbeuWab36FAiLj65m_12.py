
def grouping(w):
  ret = {}
  for word in w:
    count = sum([1 if ch.isupper() else 0 for ch in word])
    if count in ret.keys():
      ret[count].append(word)
      ret[count].sort(key=lambda x: x.lower())
    else:
      ret[count] = [word]
  return ret

