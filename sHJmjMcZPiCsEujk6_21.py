
def pilish_string(txt):
  if not txt:
    return txt
  x,res = 0,[]
  for i in map(int,'314159265358979'):
    if not txt:
      break
    res.append(txt[:i])
    txt = txt[i:]
    x = i
  while len(res[-1]) < x:
    res[-1] += res[-1][-1]
  return ' '.join(res)

