
def formula(txt):
  txt = txt.replace('=', '==').replace('a', '4')
  if not txt: return None
  return eval(txt)

