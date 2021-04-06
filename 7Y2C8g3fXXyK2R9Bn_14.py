
def keyword_cipher(key, message):
  alpha='abcdefghijklmnopqrstuvwxyz'
  tey=''
  for x in key:
    if x not in tey:
      tey+=x
  rep=''
  for x in alpha:
    if x not in tey:
      rep+=x
  kw=tey+rep
  d=dict(zip(alpha, kw))
  res=''
  for x in message:
    if x in d:
      res+=d[x]
    else:
      res+=x
  return res

