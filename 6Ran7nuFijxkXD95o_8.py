
def keyboard_shortcut(txt):
  txt = txt.replace(" Ctrl + C","#").replace(" Ctrl + V","$")
  while '$' in txt:
    r = txt.index('$')
    if '#' in txt[:r]:
      s = txt[:r].rindex('#')
      txt = txt[:r].replace('#','') + " " + txt[:s].replace('#','') + txt[r+1:]
    else: txt = txt[:r] + txt[r+1:]
  return txt.replace('#','')

