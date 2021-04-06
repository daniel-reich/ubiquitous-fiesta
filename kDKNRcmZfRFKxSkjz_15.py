
def unmix(txt):
  x = ''
  if len(txt)%2==0:
    for i in range(0,len(txt),2):
      x+=txt[i+1]+txt[i]
  else:
    for i in range(0,len(txt)-1,2):
      x+=txt[i+1]+txt[i]
    x+=txt[len(txt)-1]
  return x

