
def make_happy(txt):
  d = {':(':':)', '8(':'8)', 'x(':'x)', ';(':';)'}
  for k, v in d.items():
    txt = txt.replace(k, v)
  return txt

