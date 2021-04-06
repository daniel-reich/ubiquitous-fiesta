
def most_common_words(text, n):
  s = text.replace("'"," ").replace("\n"," ").lower()
  x = ''.join(i for i in s if i.isalpha() or i==" ").split()
  d,r = {i:x.count(i) for i in set(x)},[]
  for _ in range(min([n,len(d)])):
    r+=[max((i for i in sorted(d,key=x.index) if i not in r),key=d.get)]
  return {i:d[i] for i in r}

