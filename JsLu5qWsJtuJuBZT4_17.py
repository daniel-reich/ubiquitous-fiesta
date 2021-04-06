
def flip(txt, spec):
  s=txt.split(' ')
  k=s[-1::-1]
  if(spec=='word'):
    return " ".join(i[::-1] for i in txt.split(' ')) 
  else: 
    return " ".join(k)

