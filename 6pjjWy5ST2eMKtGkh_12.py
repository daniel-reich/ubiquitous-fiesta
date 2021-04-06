
def replace(txt, r):
  txt=list(txt)
  f=[]
  a=r[0]
  b=r[2]
  for i in range(len(txt)):
    c=ord(txt[i])
    d=ord(a)
    e=ord(b)
    if c>=d and c<=e:
      f.append("#")
    else:
      f.append(txt[i])
  return "".join(f)

