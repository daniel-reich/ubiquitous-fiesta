
def parse_code(txt):
  d = {}
  spl = txt.split("0")
  txt = list(filter(None, spl))
  d['first_name'] = txt[0]
  d['last_name'] = txt[1]
  d['id'] = txt[2]
  return d

