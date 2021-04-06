
def domino_chain(dominos):
  res = ''
  
  for i, j in enumerate(dominos):
    if j == '|' and dominos[i + 1:] not in [' ', '/']:
      res += '/'
    else:
      res += dominos[i:]
      break
      
  return res

