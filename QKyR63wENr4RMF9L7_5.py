
def tweak_letters(txt, lst):
  a=[ord(i) for i in txt]
  b=[x+y for x,y in zip(a,lst)]
  c=[]
  for j in b:
    if j>122:c.append(chr(j-26))
    elif j<97:c.append(chr(j+26))
    else:c.append(chr(j))
  return ''.join(c)

