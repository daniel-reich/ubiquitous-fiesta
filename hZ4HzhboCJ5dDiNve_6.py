
def special_reverse_string(txt):
  res = ''
  rev = [x for x in txt if x!=' ']
  for x in range(len(txt)):
    if txt[x]==' ': res+=' '
    elif txt[x].isupper():
      res+= rev.pop().upper()
    else:
      res+= rev.pop().lower()
  return res

