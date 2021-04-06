
def text_to_number_binary(txt):
  l=[]
  txt=txt.lower()
  t=txt.replace('zero','0').replace('one','1')
  r=t.split(' ')
  for i in r:
    if i=='0' or i=='1':
      l.append(i)
  s=''.join(l)    
  x=len(s)%8
  if x==0:
    return s
  return s[:-x]

