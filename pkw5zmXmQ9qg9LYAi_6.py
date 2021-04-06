
def space_message(txt):
  res = ['']
  for c in txt:
    if c == '[':
      res.append('')
    elif c == ']':
      tmp,i = res.pop(),0
      while tmp[i].isdigit():
        i += 1
      res[-1] += tmp[i:]*int(tmp[:i])
    else:
      res[-1] += c
  return res[0]

