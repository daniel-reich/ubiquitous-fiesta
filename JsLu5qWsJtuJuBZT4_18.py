
def flip(txt, spec):
  a=[]
  lst=txt.split(' ')
  if spec=='sentence':
    for p in range(len(lst)-1,-1,-1):
      a.append(lst[p])
  else:
    for i in txt.split(' '):
      a.append(i[::-1])
  return ' '.join(a)

