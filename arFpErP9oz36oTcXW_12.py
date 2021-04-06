
def secret(txt):
  txt = txt.split('.')
  return '<'+txt[0]+" class='"+' '.join(txt[1:])+"'></"+txt[0]+'>'

