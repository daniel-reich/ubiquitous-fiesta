
def missing_alphabets (str):
  sdict = {}
  a = 'abcdefghijklmnopqrstuvwxyz'
  s = ''
  
  for i in str:
    if i in sdict: sdict[i]+=1
    else: sdict[i] = 1
  
  kmax = sdict[max(sdict, key=sdict.get)]
  
  for l in a:
    if l not in sdict:
      s+=l*kmax
    elif sdict[l]<kmax:
      s+=l*(kmax-sdict[l])
      
  return s

