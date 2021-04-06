
def num_then_char(l,m=0): 
  nc=sorted(d for s in l for d in s if isinstance(d,int) or isinstance(d,float))+sorted(s for d in l for s in d if str(s).isalpha())
  for i,s in enumerate(l):
    for d in range(len(s)):
      l[i][d]=nc[m]
      m+=1
  return l

