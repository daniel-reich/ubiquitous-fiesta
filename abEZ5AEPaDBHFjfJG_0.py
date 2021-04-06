
def formula(txt):
  t=txt.replace('a','4').replace('=','==')
  return eval(t) if txt else None

