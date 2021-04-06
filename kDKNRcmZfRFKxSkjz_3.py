
def unmix(txt):
  x = (len(txt)//2)*2
  return ''.join(txt[i+1]+txt[i] for i in range(0,x,2)) +txt[x:]

