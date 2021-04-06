
def is_repeated(strn):
  r = strn.split(strn[0])[1:]
  return r.count(r[0]) if r.count(r[0]) > 1 else False

