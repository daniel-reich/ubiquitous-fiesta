
def countdown(n, txt):
  k=''
  for s in range(n, 0, -1):
    k+=str(s)+'. '
  d=txt.upper()
  return k+d+'!'

