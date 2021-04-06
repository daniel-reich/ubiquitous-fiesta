
def countdown(n, txt):
  txt = txt.upper()
  emptystring = ''
  for i in range(n,0,-1):
    emptystring = emptystring + '{}. '.format(i)
  return emptystring + txt +'!'

