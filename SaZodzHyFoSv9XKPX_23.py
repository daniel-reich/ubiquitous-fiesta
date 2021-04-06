
def domino_chain(dominos):
  s,rem='',dominos
  for x in dominos:
    if x=='|':
      s+='/'
      rem=rem[1:] 
    else: return s+rem
  return s

