
def isWordChain(words):
  for i in range(1,len(words)):
    if len(words[i-1])==len(words[i]) and sum(a!=b for a,b in zip(words[i-1],words[i]))==1:
      continue
    elif len(words[i])-len(words[i-1])==1:
      for c in words[i-1]:
        if c not in words[i]:
          return False
        else:
          continue
    elif len(words[i-1])-len(words[i])==1:
      for c in words[i]:
        if c not in words[i-1]:
          return False
        else:
          continue
    else:
      return False
  return True

