
def make_happy(txt):
  d = {':(':':)','8(':'8)','x(':'x)',';(':';)'}
  for k in d.keys():
    txt = txt.replace(k,d[k])
  return txt

