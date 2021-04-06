
def domino_chain(dominos):
  ans=''
  for i in range(len(dominos)):
    if dominos[i]=='|':ans+='/'
    else:return ans+dominos[i:]
  return ans

