
def keyboard_shortcut(txt):
  copy = []
  txt = txt.replace('Ctrl + V','Ctrl+V').replace('Ctrl + C','Ctrl+C').split()
  ret = []
  for i in txt:
    if i!='Ctrl+V' and i!='Ctrl+C':
      ret.append(i)
    elif i=='Ctrl+C':
      copy = [i for i in ret]
    elif i=='Ctrl+V':
      if copy:
        ret+=copy
  return ' '.join(ret)

