
def is_sorted(words, alphabet):
  
  alph = dict()
  
  for i in range(0,len(alphabet)):
    alph[alphabet[i]]=i
    
    
  new_l = []
  
  for x in words:
    s=""
    for i in range(0,len(x)):
      s+=chr(alph[x[i]]+97)
    new_l.append(s)
  
  return sorted(new_l)==new_l

