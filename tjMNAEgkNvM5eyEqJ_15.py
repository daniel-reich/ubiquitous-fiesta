
def unique_abbrev(abbs, words):
  a=len(abbs)
  b=len(words)
  cnt=0
  ok=0
  for i in range(0,a):
    c=abbs[i]
    d=len(c)
    for j in range(0,b):
      e=words[j]
      f=len(e)
      if(c==e[0:d]):
        cnt=cnt+1
    if(cnt>1):
      return False
    cnt=0
  return True

