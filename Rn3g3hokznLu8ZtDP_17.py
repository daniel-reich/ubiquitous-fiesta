
def increment_string(txt):
  b="0123456789"
  s=""
  v=""
  z=""
  c=0
  switch=False
  if txt[len(txt)-1] not in b:
    txt=txt+"1"
    return txt
  for t in txt:
    if t=="0" and switch==False:
      s=s+"0"
    elif t in b:
      c+=1
      switch=True
      v=v+t
    else:
      z=z+t
  v=int(v)+1
  if len(str(v))>c:
    if len(s)>0:
      s=s[:len(s)-1]
  z=z+s+str(v)
  return z

