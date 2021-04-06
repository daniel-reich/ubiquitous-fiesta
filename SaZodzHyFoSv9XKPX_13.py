
def domino_chain(dominos):
  falling, res = True, ''
  
  for i in dominos:
    if i == '|' and falling:
      res += '/'
    else:
      res += i
      falling = False
      
  return res

