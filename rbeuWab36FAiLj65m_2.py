
def grouping(words):
  words.sort(key=lambda x:x.lower())
  res={}
  for w in words:
    n=sum(c.isupper() for c in w)
    if n in res:res[n]+=[w]
    else:res[n]=[w]
  return res

