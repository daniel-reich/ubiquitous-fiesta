
def to_scottish_screaming(txt):
  d = dict()
  d['a'] = 'E'
  d['e'] = 'E'
  d['i'] = 'E'
  d['o'] = 'E'
  d['u'] = 'E'
  s = ""
  ss = list(txt.strip())
  for elem in ss:
    if(elem.isalpha()):
      k = elem.lower()
      if(k in d):
        s += d[k]
      else:
        s += k.upper()
    else:
      s += elem
  return s

