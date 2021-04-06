
def unstretch(word):
  c=word[0]
  for i in range(1,len(word)):
    if word[i]!=c[-1]:
      c+=word[i]
  return c

