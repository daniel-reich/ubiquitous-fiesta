
def playfair(txt, key):
  dr = -1 if txt.isupper() else 1
  key = key.replace("j","i")
  txt = "".join(l.upper() for l in txt if l.isalpha()).replace("J","I") 
  alp_plain = "abcdefghiklmnopqrstuvwxyz"
  alp = "".join(sorted(alp_plain,key = (key+alp_plain).index)).upper()
  poly = {(i,j):alp[i*5+j] for j in range(5) for i in range(5)}
  unpoly = {l:t for t,l in poly.items()}
  
  digs,i = [],0
  while i < len(txt):
    if i == len(txt)-1: 
      digs+= [txt[i]+"X"]
      i+=1
    elif txt[i]!=txt[i+1]: 
      digs+= [txt[i:i+2]]
      i+=2
    else: 
      digs+= [txt[i]+"X"]
      i+=1
    
  def en_dig(d):
    (x1,y1), (x2,y2) = unpoly[d[0]], unpoly[d[1]]
    a,b = ((x1+dr*(y1==y2))%5,y2*(x1!=x2)+((y1+dr)%5)*(x1==x2))
    c,d = ((x2+dr*(y1==y2))%5,y1*(x1!=x2)+((y2+dr)%5)*(x1==x2))
    return poly[(a,b)]+poly[(c,d)]
    
  return "".join([en_dig(d) for d in digs])

