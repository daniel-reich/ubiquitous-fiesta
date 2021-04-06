
def formula(txt):
  if not txt:
    return None
  a = 4
  return eval(txt.replace('=','=='))

