
def split(txt):
  marker = 0
  s = []
  clusters = []
  
  for c in txt:
    if c == '(':
      s.append(c)
    elif c == ')':
      s.pop()
    marker += 1
    #..... EZ CLAP
    if len(s) == 0:
      clusters.append(txt[0: marker])
      txt = txt[marker:]
      marker = 0
  
  return clusters

