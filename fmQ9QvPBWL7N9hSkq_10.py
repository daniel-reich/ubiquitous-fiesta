
def unstretch(word):
  k=word[0]
  for i in range(1,len(word)):
    if(word[i]!=word[i-1]):
      k+=word[i]
  return k

