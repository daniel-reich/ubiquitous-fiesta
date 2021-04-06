
def cap_space(txt):
  ss = map(str, txt.strip())
  res = []
  i = 0
  for elem in ss:
    if(i!= 0):
      if(elem.isupper()):
        res.append(' ')
        res.append(elem.lower())
      else:
        res.append(elem)
    else:
      res.append(elem)
    i += 1
    
  r = ""
  for elem in res:
    r += str(elem)
  return r

