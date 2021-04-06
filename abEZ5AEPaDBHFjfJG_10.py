
def formula(txt):
  txt = txt.replace(' ','')
  txt = txt.replace('a','4')
  if txt == '':
    return None
  for i in txt.split('='):
    if eval(i)!=eval(txt.split('=')[0]):
      return False
  return True

