
def soroban(l):
  d=""
  for i in [[i[k] for i in l ] for k in range(7)]:
    if i[0]=='|' and i[3]=='|':
      d+=str(5)
    elif i[0]=='|' and i[4]=='|':    
      d+=str(6)
    elif i[0]=='|' and i[5]=='|':    
      d+=str(7)
    elif i[0]=='|' and i[6]=='|':    
      d+=str(8)
    elif i[0]=='|' and i[7]=='|':    
      d+=str(9)
    elif i[1]=='|' and i[4]=='|':    
      d+=str(1)
    elif i[1]=='|' and i[5]=='|':    
      d+=str(2)
    elif i[1]=='|' and i[6]=='|':    
      d+=str(3)
    elif i[1]=='|' and i[7]=='|':    
      d+=str(4)
    else:    
      d+=str(0)
  return int(d)

