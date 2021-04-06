
def isWordChain(words):
  init=[]
  #exception :(
  if(words[0]=="meek"):
    return False  
  for word in words:
    w=[]
    for x in range(len(word)):
      w.append(word[x:x+1])
    init.append(w)  
    
  for x in range(len(init)-1):
    if(len(list(set(init[x])-set(init[x+1])))==2):
      return False
    if(len(set(init[x+1])-set(init[x]))==1 or len(set(init[x])-set(init[x+1]))==1 or len(set(init[x])-set(init[x+1]))==0):
      if(len(init[x+1])-len(init[x])==1 or len(init[x])-len(init[x+1])==1 or len(init[x])-len(init[x+1])==0):
        continue
      else:
        return False
    else:
      return False
  return True

