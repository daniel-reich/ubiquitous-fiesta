
def strip_url_params(url, params_to_strip=[]):
  fields = url.split('?')
  addr = fields[0]
  s = addr
  if len(fields) <= 1:
    return s
  s += '?'  
  field = fields[1].split('&')
  d = dict()
  l = []
  for f in field:
    tokens = f.split('=')
    if tokens[0] not in params_to_strip:
      if tokens[0] not in l:
        l.append(tokens[0])
      d[tokens[0]] = tokens[1]  
  for i in range(len(l)):
    key = l[i]
    s += key + '=' + d[key]
    if i < len(l) - 1:
      s += '&'
  return s

