
def formula(txt):
  t = txt.replace("=","==")
  a = 4
  return eval(t) if t else None

