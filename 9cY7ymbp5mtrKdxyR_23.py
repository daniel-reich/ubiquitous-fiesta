
def encryption(txt):
  txt = txt.replace(' ','')
  L = int(round(len(txt)**(1/2),0))
  if L**2 < len(txt):
    L += 1
  txt = [txt[i:i+L] for i in range(0,len(txt),L)]
  lst = []
  for i in range(L):
    lst.append(''.join([x[i] if len(x)>i else '' for x in txt]))
  return ' '.join(lst)

