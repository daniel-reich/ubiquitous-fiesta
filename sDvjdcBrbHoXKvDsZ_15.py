
def anagram(name, words):
  i = 0
  j = 0
  name = list(name.lower().replace(' ',''))
  while i < len(words):
    while j < len(words[i]):
      if words[i][j] not in name:
        return False
      else:
        name.remove(words[i][j])
      j += 1
    j = 0
    i += 1
  if len(name) > 0:
    return False
  return True

