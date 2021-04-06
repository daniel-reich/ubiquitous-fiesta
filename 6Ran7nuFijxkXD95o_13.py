
def keyboard_shortcut(txt):
  txt=txt.replace('Ctrl + V','Ctrl+V')
  txt=txt.replace('Ctrl + C','Ctrl+C')
  running=copied=out=''
  CC,w=0,False
  for word in txt.split():
    if word=='Ctrl+C':
      if w:
        copied+=running
      else:
        copied+=copied
      CC+=1
      w=False
      if CC>1:
        copied=''
    elif word=='Ctrl+V':
      if not copied=='':
        out+=copied + ' '
      CC=0
    else:
      running+=word + ' '
      out+= word + ' '
      w=True
  return ' '.join(out.split())

