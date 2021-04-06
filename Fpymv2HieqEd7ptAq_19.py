
def split(txt):
  i=0
  s=""
  l=[]
  for char in txt:
    if char == "(":
      i+=1
      s+="("
    elif char == ")":
      i-=1
      s+=")"
    if i==0:
      l.append(s)
      s=""
  return l

