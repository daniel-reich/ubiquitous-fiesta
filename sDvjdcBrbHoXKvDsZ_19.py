
def anagram(name, words):
  l = []
  for i in range(len(name)):
    if name[i] != ' ':
      l.append(name[i].lower())
  for i in range(len(words)):
    for j in range(len(words[i])):
      if words[i][j].lower() in l:
        l.remove(words[i][j])
      else:
        return False
  if len(l) == 0:
    return True
  else:
    return False

