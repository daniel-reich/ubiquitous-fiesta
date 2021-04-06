
def elasticize(word):
  if len(word)<3: return word
  m = int(len(word)/2)
  w = ''
  if len(word)%2:
    for x in range(m+1):  w+=word[x]*(x+1)
    for i in range(m-1,-1,-1): w+=word[::-1][i]*(i+1)
  else:
    for x in range(m):  w+=word[x]*(x+1)
    for i in range(m-1,-1,-1): w+=word[::-1][i]*(i+1)
  return w

