
def can_build(a,b):
  l=len(a)
  for x in b:
    a=a.replace(x,'',1)
  return l==len(a)+len(b)

