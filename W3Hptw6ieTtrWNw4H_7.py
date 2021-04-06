
def bifid(text):
  alp = "abcdefghiklmnopqrstuvwxyz"
  
  if " " in text:
    text = "".join(l for l in text.lower() if l.isalpha())
    ns = [alp.index(l)//5 for l in text] + [alp.index(l)%5 for l in text]
    return "".join(alp[ns[i]*5+ns[i+1]] for i in range(0,len(ns),2))
    
  ns = sum(([alp.index(l)//5,alp.index(l)%5] for l in text),[])
  return "".join(alp[ns[i]*5+ns[i+len(ns)//2]] for i in range(len(ns)//2))

