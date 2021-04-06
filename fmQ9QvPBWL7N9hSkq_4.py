
def unstretch(word):
  ret = [word[0]]
  for i in range(1,len(word)):
    if word[i]!=word[i-1]:
      ret.append(word[i])
  return ''.join(ret)

