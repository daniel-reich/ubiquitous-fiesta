
def neighboring(txt):
  return all(abs(ord(x)-ord(y))==abs(ord(y)-ord(z))==1 for x,y,z in zip(txt,txt[1:],txt[2:]))

