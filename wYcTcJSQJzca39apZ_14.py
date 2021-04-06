
def truncate(txt, length):
  wds = txt.split()
  n = 0
  res = ''
  for w in wds:
    n += len(w) + 1
    if n <= length+1:
      res = res + w + ' '
  return res[:-1]

