
def elasticize(word):
  s = ""
  for i in range(0, len(word)):
    if i >= len(word) / 2:
      s += (len(word) - i) * word[i]
    else:
      s += (i + 1) * word[i]
  return s

