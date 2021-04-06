
def domino_chain(dominos):
  if '|' in dominos:
    res=''
    i=0
    while dominos[i]=='|':
      res+='/'
      i+=1
      if i>=len(dominos):
        break
    if i==len(dominos):
      return res
    else: 
      res+=dominos[i:]
      return res
  else:
    return dominos

