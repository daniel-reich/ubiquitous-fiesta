
def flip(s):
  for i in range(len(s)):
    if s[i]==1:
      s[i]=0
    elif s[i]==0:
      s[i]=1
def freed_prisoners(prison):
  p=prison
  f=0
  if p[0]==0:
    return 0
  else:
    for i in range(len(p)):
      if p[i]==1:
        f+=1
        flip(p)
  return f

