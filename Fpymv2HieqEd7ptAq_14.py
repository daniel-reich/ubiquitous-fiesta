
def split(txt):
  lst = []
  count = 0
  cluster = ''
  for ch in txt:
    if ch == '(':
      cluster += ch
      count += 1
    else:
      cluster += ch
      count -=1
    if count == 0:
      lst.append(cluster)
      cluster = ''
  return lst

